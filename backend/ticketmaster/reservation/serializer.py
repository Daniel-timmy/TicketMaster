import qrcode
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
        fields = (
            "id",
            "reservation_name",
            "groups",
            "spaces_per_group",
            "recurring_event",
            "ticket_data",
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

