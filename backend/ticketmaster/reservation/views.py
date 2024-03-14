from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from .models import Reservation, ReservationBooking
from .serializer import ReservationSerializer, ReservationBookingSerializer
from .permissions import IsCreatorOrReadOnly
"""
This module define the CRUD operations of the API for reservation
"""


class ReservationList(generics.ListCreateAPIView):
    """
    ReservationList class defines an API endpoint for handling HTTP GET requests to list existing
    reservations and HTTP POST requests to create new reservation.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = ReservationSerializer

    def get_queryset(self):
        """
        Filter reservations related to the currently logged-in user
        """
        return Reservation.objects.filter(creator=self.request.user)


class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    ReservationList class defines an API endpoint for handling HTTP GET, PUT, and DELETE requests
    on a single reservation instance.
    """
    permission_classes = (IsCreatorOrReadOnly,)
    serializer_class = ReservationSerializer

    def get_queryset(self):
        """
        Filter reservation related to the currently logged-in user
        """
        return Reservation.objects.filter(creator=self.request.user)


class ReservationBookingList(generics.ListAPIView):
    """
    ReservationBookingList class defines an API endpoint for handling HTTP GET requests to list existing
    reservation-bookings
    """
    permission_classes = (IsAuthenticated,)
    queryset = ReservationBooking.objects.all()
    serializer_class = ReservationBookingSerializer


class ReservationBookingCreate(generics.CreateAPIView):
    """
    ReservationBookingCreate class defines an API endpoint for handling
    HTTP POST requests to create new reservation-bookings.
    """
    permission_classes = (AllowAny,)
    queryset = ReservationBooking.objects.all()
    serializer_class = ReservationBookingSerializer


class ReservationBookingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    ReservationBookingDetail class defines an API endpoint for handling HTTP GET, PUT, and DELETE requests
    on a single reservation-booking instance.
    """
    permission_classes = (IsAuthenticated,)
    queryset = ReservationBooking.objects.all
    serializer_class = ReservationBookingSerializer
