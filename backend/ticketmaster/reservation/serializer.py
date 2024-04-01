import uuid

import qrcode
from django.contrib.auth import get_user
from rest_framework import serializers

from .models import Reservation, ReservationBooking

"""
This module defines the serializers used for the Reservations
and ReservationsBookings model
"""


def generate_ticket_data(no_of_tickets):
    """

    :param no_of_tickets: number of tickets required by the user for the event
    :return: list of ticket with the following information
    ticket_id, available, and attendee_id
    """
    ticket_list = []

    for i in range(0, int(no_of_tickets)):
        t_data = {"ticket_id": str(uuid.uuid4()),
                  "available": True,
                  "attendee_id": None}
        ticket_list.append(t_data)
    return ticket_list


def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img_bytes = img.tobytes()
    return img_bytes


class ReservationSerializer(serializers.ModelSerializer):
    """
     ReservationSerializer class defines a
    serializer for handling serialization
    and deserialization of reservation data.
    """
    # reservation_booking = serializers.PrimaryKeyRelatedField(
    #     many=True, queryset=ReservationBooking.objects.all())
    total_cost = serializers.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        model = Reservation
        fields = (
            "id",
            "reservation_name",
            "groups",
            "spaces_per_group",
            "recurring_event",
            "start_date",
            "start_time",
            "end_date",
            "end_time",
            "venue_name",
            "venue_address",
            "venue_country",
            "online_event",
            "description",
            'total_cost',
        )

    def create(self, validated_data):
        """

        :param validated_data:
        :return:
        """

        no_of_tickets = validated_data['groups'] * validated_data['spaces_per_group']
        total_cost = validated_data.pop('total_cost', None)
        ticket_data = generate_ticket_data(no_of_tickets)
        validated_data['ticket_data'] = ticket_data
        user = self.context['request'].user
        creator = get_user(self.context['request'])
        validated_data['creator'] = creator
        validated_data['email'] = user

        return Reservation.objects.create(**validated_data)


class ReservationBookingSerializer(serializers.ModelSerializer):
    """
    ReservationsBookingsSerializer class defines a
    serializer for handling serialization
    and deserialization of reservation-bookings data.
    """

    class Meta:
        model = ReservationBooking
        fields = (
            "id",
            "reservation",
            "customer_name",
            "email",
            'group_name',
            'space_name',
            "start_date",
            "start_time",
            "end_date",
            "end_time",
            "event_type"
        )

    def create(self, validated_data):
        """

        :param validated_data:
        :return:
        """
        data_dict = validated_data.copy()
        data_dict['qr_code'] = generate_qr_code(data_dict)
        return ReservationBooking.objects.create(**data_dict)

