from rest_framework import generics
from .models import Event, EventBooking
from .serializer import EventSerializer, EventBookingSerializer
from .permissions import IsCreatorOrReadOnly
from rest_framework.permissions import IsAuthenticated, AllowAny

"""
This module define the CRUD operations of the API for events
"""


class EventList(generics.ListCreateAPIView):
    """
    EventsList class defines an API endpoint for handling HTTP GET requests to list existing
    events and HTTP POST requests to create new event.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = EventSerializer

    def get_queryset(self):
        """
        Filter events related to the currently logged-in user
        """
        return Event.objects.filter(creator=self.request.user)


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
