import uuid

from django.db import transaction
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from .models import Reservation, ReservationBooking
from .serializer import ReservationSerializer, ReservationBookingSerializer
from .permissions import IsCreatorOrReadOnly

"""
This module define the CRUD operations of the API for reservation
"""


def generate_ticket_data(no_of_tickets):
    """

    :param no_of_tickets: number of tickets required by the user for the event
    :return: list of ticket with the following information
    ticket_id, available, and attendee_id
    """
    ticket_list = []
    for i in range(no_of_tickets):
        t_data = {"ticket_id": uuid.uuid4(),
                  "available": True,
                  "attendee_id": None}
        ticket_list.append(t_data)
    return ticket_list


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

    def perform_create(self, serializer):
        """
        This method is called when a new resource instance is being created.
        It prepares necessary data and saves the instance using the provided serializer.

        :param serializer:Serializer instance. Used for validating and saving data.
        :return: None
        """
        data = self.request.data.copy()
        no_of_tickets = int(data['no_of_tickets'])
        with transaction.atomic():
            ticket_data = generate_ticket_data(no_of_tickets)
            serializer.save(ticket_data=ticket_data)


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
