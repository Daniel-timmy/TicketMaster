from rest_framework import generics
from .models import Event, EventBooking
from .serializer import EventSerializer, EventBookingSerializer
from .permissions import IsCreatorOrReadOnly
"""
This module define the CRUD operations of the API for events
"""


class EventList(generics.ListCreateAPIView):
    """
    EventsList class defines an API endpoint for handling HTTP GET requests to list existing events
    and HTTP POST requests to create new events.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    EventDetail class defines an API endpoint for handling HTTP GET, PUT, and DELETE requests
    on a single event instance.
    """
    permission_classes = (IsCreatorOrReadOnly,)
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventBookingList(generics.ListCreateAPIView):
    """
     EventBookingsList class defines an API endpoint for handling HTTP GET, PUT, and DELETE requests
    on a single event-booking instance.
    """
    queryset = EventBooking.objects.all()
    serializer_class = EventBookingSerializer


class EventBookingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    EventBookingsDetail class defines an API endpoint for handling HTTP GET, PUT, and DELETE requests
    on a single event-booking instance.
    """
    queryset = EventBooking.objects.all()
    serializer_class = EventBookingSerializer
