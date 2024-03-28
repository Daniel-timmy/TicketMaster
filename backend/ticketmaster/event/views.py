import uuid

from django.db import transaction
from django.utils.dateparse import parse_date, parse_time
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


def generate_ticket_data(no_of_tickets):
    """

    :param no_of_tickets: number of tickets required by the user for the event
    :return: list of ticket with the following information
    ticket_id, available, and attendee_id
    """
    ticket_list = []

    for i in range(0, int(no_of_tickets)):
        t_data = {"ticket_id": uuid.uuid4(),
                  "available": True,
                  "attendee_id": None}
        ticket_list.append(t_data)
    return ticket_list


class EventCreate(generics.CreateAPIView):
    """
    EventCreate class defines an API endpoint for handling HTTP POST for creating a new event and
    generating all associated tickets.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = EventSerializer

    # def perform_create(self, serializer):
    #     """
    #     This method is called when a new resource instance is being created.
    #     It prepares necessary data and saves the instance using the provided serializer.
    #
    #     :param serializer:Serializer instance. Used for validating and saving data.
    #     :return: None
    #     """
    #     data = self.request.data.copy()
    #     no_of_tickets = data.pop('no_of_tickets')[0]
    #     total_cost = data.pop('total_cost', None)
    #     stripe_token = data.pop('stripe_token', None)
    #
    #     with transaction.atomic():
    #         ticket_data = generate_ticket_data(no_of_tickets)
    #         print(data)
    #         serializer.save(ticket_data=ticket_data)

    def create(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = self.request.data.copy()
        no_of_tickets = data['no_of_tickets'][0]
        total_cost = data['total_cost']
        stripe_token = data['stripe_token']
        # data.pop('csrfmiddlewaretoken')
        ticket_data = generate_ticket_data(no_of_tickets)
        data['ticket_data'] = ticket_data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer=serializer)
        # event = serializer.save()

        return Response({'message': 'Event creation sucessful'})
            

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
