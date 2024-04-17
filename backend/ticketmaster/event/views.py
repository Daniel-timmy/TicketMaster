import copy
from smtplib import SMTPException
from django.core.mail import send_mail, BadHeaderError
from django.db import transaction
from psycopg2 import IntegrityError
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .models import Event, EventBooking
from .serializer import EventSerializer, EventBookingSerializer, EventListSerializer
from .permissions import IsCreatorOrReadOnly
from rest_framework.permissions import IsAuthenticated, AllowAny

"""
This module define the CRUD operations of the API for events
"""


def event_email(subject, msg, from_email, receive_email):
    """

    :param subject:
    :param msg:
    :param from_email:
    :param receive_email:
    :return:
    """
    try:
        send_mail(
            subject=subject,
            message=msg,
            from_email=from_email,
            recipient_list=[receive_email],
            fail_silently=False,
        )
        return True
    except (BadHeaderError, SMTPException):
        raise


class EventList(generics.ListAPIView):
    """
    EventsList class defines an API endpoint for handling HTTP GET requests to list existing
    events.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = EventListSerializer

    def get_queryset(self):
        """
        Filter events related to the currently logged-in user
        """
        return Event.objects.filter(creator=self.request.user)


class EventCreate(generics.CreateAPIView):
    """
    EventCreate class defines an API endpoint for handling HTTP POST for creating a new event and
    generating all associated tickets.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = EventSerializer

    def post(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = copy.deepcopy(request.data)

        serializer = self.get_serializer(data=data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            with transaction.atomic():
                try:
                    instance = serializer.save()
                except (ValidationError, IntegrityError, Exception):
                    return Response({'message': 'Event creation failed'}, status=status.HTTP_400_BAD_REQUEST)
                try:
                    result = event_email(subject=instance.event_name, msg="Success",
                                         from_email='ajayitimmy45@gmail.com', receive_email=instance.email)
                except (BadHeaderError, SMTPException):
                    return Response({'mail_status': result, 'message': 'Email error'},
                                    status=status.HTTP_400_BAD_REQUEST)
            return Response({'message': 'Event creation successful', 'event': instance, 'email': 'Check your mail for '
                                                                                                 'the event details'},
                            status=status.HTTP_201_CREATED)

        return Response({'message': 'Event creation failed'}, status=status.HTTP_400_BAD_REQUEST)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    EventDetail class defines an API endpoint for handling HTTP GET, PUT, and DELETE requests
    on a single event instance.
    """
    permission_classes = (IsCreatorOrReadOnly,)
    serializer_class = EventSerializer

    def get_queryset(self):
        """
        Filter events related to the currently logged-in user
        """
        return Event.objects.filter(creator=self.request.user)


class EventBookingList(generics.ListAPIView):
    """
    EventBookingList class defines an API endpoint for handling HTTP GET requests to list existing
    event bookings
    """
    permission_classes = (IsAuthenticated,)
    queryset = EventBooking.objects.all()
    serializer_class = EventBookingSerializer


class EventBookingCreate(generics.CreateAPIView):
    """
    EventBookingCreate class defines an API endpoint for handling HTTP POST requests
    on a single event-booking instance.
    """
    permission_classes = (AllowAny,)
    queryset = EventBooking.objects.all()
    serializer_class = EventBookingSerializer

    def post(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        event_name = kwargs.get('event_name', None)
        event = Event.objects.filter(event_name=event_name)
        if event is None:
            return Response({'message': 'Event does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data, context={'event': event})
        if serializer.is_valid(raise_exception=True):
            with transaction.atomic():
                try:
                    instance, qc = serializer.save()
                    mail = event_email(subject=event.event_name, msg=qc, from_email=event.creator, receive_email=instance.email)
                except:
                    return Response({'message': 'Failed to register your booking'})
            return Response({'message': 'Successful', 'booking': instance}, status=status.HTTP_201_CREATED)
        return Response({'message': 'Failed to create event due to validation errors.'},
                        status=status.HTTP_400_BAD_REQUEST)


class EventBookingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    EventBookingsDetail class defines an API endpoint for handling HTTP GET, PUT, and DELETE requests
    on a single event-booking instance.
    """
    permission_classes = (IsAuthenticated,)
    queryset = EventBooking.objects.all()
    serializer_class = EventBookingSerializer
