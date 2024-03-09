from django.shortcuts import render
from rest_framework import generics
from .models import Reservation, ReservationBooking
from .serializer import ReservationSerializer, ReservationBookingSerializer
from .permissions import IsCreatorOrReadOnly
"""

"""


class ReservationList(generics.ListCreateAPIView):
    """

    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationBookingDetail(generics.RetrieveUpdateDestroyAPIView):
    """

    """
    permission_classes = (IsCreatorOrReadOnly,)
    queryset = ReservationBooking.objects.all
    serializer_class = ReservationBookingSerializer
