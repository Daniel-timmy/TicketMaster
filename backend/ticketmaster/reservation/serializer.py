from rest_framework import serializers

from .models import Reservation, ReservationBooking

"""
This module defines the serializers used for the Reservations
and ReservationsBookings model
"""


class ReservationSerializer(serializers.ModelSerializer):
    """
     ReservationSerializer class defines a
    serializer for handling serialization
    and deserialization of reservation data.
    """
    reservation_booking = serializers.PrimaryKeyRelatedField(
        many=True, queryset=ReservationBooking.objects.all())

    class Meta:
        model = Reservation
        fields =(
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
            "reservation_booking",
        )


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
            "alpha_numeric",
            "QR_code",
            "start_date",
            "start_time",
            "end_date",
            "end_time",
            "event_type"
        )