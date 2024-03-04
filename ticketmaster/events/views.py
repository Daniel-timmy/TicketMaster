from rest_framework import generics
from .models import Events, EventsBookings
from .serializer import EventsSerializer, EventsBookingsSerializer
"""
This module define the CRUD operations of the API for events
"""


class EventsList(generics.ListCreateAPIView):
    """
    EventsList class defines an API endpoint for handling HTTP GET requests to list existing events
    and HTTP POST requests to create new events.
    """
    queryset = Events.objects.all()
    serializer_class = EventsSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    EventDetail class defines an API endpoint for handling HTTP GET, PUT, and DELETE requests
    on a single event instance.
    """
    queryset = Events.objects.all()
    serializer_class = EventsSerializer


class EventsBookingsList(generics.ListCreateAPIView):
    """
     EventBookingsList class defines an API endpoint for handling HTTP GET, PUT, and DELETE requests
    on a single event-booking instance.
    """
    queryset = EventsBookings.objects.all()
    serializer_class = EventsBookingsSerializer


class EventsBookingsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    EventBookingsDetail class defines an API endpoint for handling HTTP GET, PUT, and DELETE requests
    on a single event-booking instance.
    """
    queryset = EventsBookings.objects.all()
    serializer_class = EventsBookingsSerializer
