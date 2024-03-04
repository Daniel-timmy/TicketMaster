from rest_framework import serializers

from ticketmaster.reservations.models import Reservations, ReservationBookings

"""
This module defines the serializers used for the Reservations
and ReservationsBookings model
"""


class ReservationsSerializer(serializers.ModelSerializer):
    """
     ReservationSerializer class defines a
    serializer for handling serialization
    and deserialization of reservation data.
    """
    reservation_bookings = serializers.PrimaryKeyRelatedField(
        many=True, queryset=ReservationBookings.objects.all())
    class Meta:
        model = Reservations
        fields =(
            "id",
            "creator",
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
            "description"
        )


class ReservationBookingsSerializer(serializers.ModelSerializer):
    """
    ReservationsBookingsSerializer class defines a
    serializer for handling serialization
    and deserialization of reservation-bookings data.
    """
    class Meta:
        model = ReservationBookings
        fields = (
            "id",
            "reservation",
            "customer_name",
            "email",
            "alpha_numeric",
            "QR_code",
            "start_date",
            "start_time",
            "end_date",
            "end_time",
            "event_type"
        )