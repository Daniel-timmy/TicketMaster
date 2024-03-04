from .models import Events, EventsBookings
from rest_framework import serializers

"""
This module defines the serializers used for the Events
and EventsBookings model
"""


class EventsSerializer(serializers.ModelSerializer):
    """
    EventsSerializer class defines a
    serializer for handling serialization
    and deserialization of event data.
    """
    events_bookings = serializers.PrimaryKeyRelatedField(
        many=True, queryset=EventsBookings.objects.all())

    class Meta:
        model = Events
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


class EventsBookingsSerializer(serializers.ModelSerializer):
    """
    EventsBookingsSerializer class defines a
    serializer for handling serialization
    and deserialization of event-bookings data.
    """

    class Meta:
        model = EventsBookings
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
