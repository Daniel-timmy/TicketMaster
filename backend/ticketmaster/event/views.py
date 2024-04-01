import copy
import uuid

from django.contrib.auth import get_user_model, get_user

from rest_framework import generics
from rest_framework.response import Response

from .models import Event, EventBooking
from .serializer import EventSerializer, EventBookingSerializer, EventListSerializer
from .permissions import IsCreatorOrReadOnly
from rest_framework.permissions import IsAuthenticated, AllowAny

"""
This module define the CRUD operations of the API for events
"""


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
            instance = serializer.save()
            return Response({'message': 'Event creation sucessful'})

        return Response({'message': 'Event creation failed'})


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


class EventBookingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    EventBookingsDetail class defines an API endpoint for handling HTTP GET, PUT, and DELETE requests
    on a single event-booking instance.
    """
    permission_classes = (IsAuthenticated,)
    queryset = EventBooking.objects.all()
    serializer_class = EventBookingSerializer
