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
    event_booking = serializers.PrimaryKeyRelatedField(
        many=True, queryset=EventBooking.objects.all())

    class Meta:
        model = Event
        fields = ('id',
                  'event_name',
                  'tickets',
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
                  'event_type')


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
            'alpha_numeric',
            'QR_code',
            'start_date',
            'start_time',
            'end_date',
            'end_time',
            'event_type',)
