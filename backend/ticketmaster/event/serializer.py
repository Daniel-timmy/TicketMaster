import qrcode

from .models import Event, EventBooking
from rest_framework import serializers

"""
This module defines the serializers used for the Events
and EventBooking model
"""


class EventSerializer(serializers.ModelSerializer):
    """
    EventSerializer class defines a
    serializer for handling serialization
    and deserialization of event data.
    """
    total_cost = serializers.DecimalField(max_digits=6, decimal_places=2)
    stripe_token = serializers.CharField(max_length=200)
    no_of_tickets = serializers.IntegerField()

    class Meta:
        model = Event
        fields = ('id',
                  'event_name',
                  'start_date',
                  'start_time',
                  'end_date',
                  'end_time',
                  'venue_name',
                  'venue_address',
                  'venue_country',
                  'online_event',
                  'recurring_event',
                  'description',
                  'total_cost',
                  'stripe_token',
                  'no_of_tickets'
                  )
        read_only_fields = ('total_cost', 'stripe_token', 'no_of_tickets')


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


class EventBookingSerializer(serializers.ModelSerializer):
    """
    EventBookingSerializer class defines a
    serializer for handling serialization
    and deserialization of event-bookings data.
    """

    class Meta:
        model = EventBooking
        fields = (
            'id',
            'customer_name',
            'email',
            'event',
            'start_date',
            'start_time',
            'end_date',
            'end_time',
            'event_type',)

    def create(self, validated_data):
        """

        :param validated_data:
        :return:
        """
        data_dict = validated_data.copy()
        data_dict['qr_code'] = generate_qr_code(data_dict)
        return EventBooking.objects.create(**data_dict)


class EventListSerializer(serializers.ModelSerializer):
    """
    EventSerializer class defines a
    serializer for handling serialization
    and deserialization of event data.
    """
    event_booking = serializers.PrimaryKeyRelatedField(
        many=True, queryset=EventBooking.objects.all())

    class Meta:
        model = Event
        fields = ('id',
                  'event_name',
                  'start_date',
                  'start_time',
                  'end_date',
                  'end_time',
                  'venue_name',
                  'venue_address',
                  'venue_country',
                  'online_event',
                  'recurring_event',
                  'description',
                  'event_booking',
                  )

