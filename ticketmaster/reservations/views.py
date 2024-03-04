from django.shortcuts import render
from rest_framework import generics
from ticketmaster.reservations.models import Reservations

"""

"""


class ReservationList(generics.ListCreateAPIView):
    """

    """
    queryset = Reservations.objects.all()
    serializer_class =