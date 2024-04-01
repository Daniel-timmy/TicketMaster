import copy
import uuid

from django.db import transaction
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from rest_framework.response import Response

from .models import Reservation, ReservationBooking
from .serializer import ReservationSerializer, ReservationBookingSerializer
from .permissions import IsCreatorOrReadOnly

"""
This module define the CRUD operations of the API for reservation
"""


class ReservationList(generics.ListAPIView):
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


class ReservationCreate(generics.CreateAPIView):
    """
    ReservationCreate class defines an API endpoint for handling HTTP POST for creating a new Reservation and
    generating all associated tickets.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = ReservationSerializer

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
