import uuid
import qrcode
from .models import Event, EventBooking
from rest_framework import serializers
from django.contrib.auth import get_user

"""
This module defines the serializers used for the Events
and EventBooking model
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


class EventSerializer(serializers.ModelSerializer):
    """
    EventSerializer class defines a
    serializer for handling serialization
    and deserialization of event data.
    """
    total_cost = serializers.DecimalField(max_digits=6, decimal_places=2)
    no_of_tickets = serializers.IntegerField(required=False)

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
                  'no_of_tickets'
                  )

    def create(self, validated_data):
        """

        :param validated_data:
        :return:
        """

        no_of_tickets = validated_data.pop('no_of_tickets')
        total_cost = validated_data.pop('total_cost', None)
        ticket_data = generate_ticket_data(no_of_tickets)
        validated_data['ticket_data'] = ticket_data
        user = self.context['request'].user
        creator = get_user(self.context['request'])
        validated_data['creator'] = creator
        validated_data['email'] = user

        return Event.objects.create(**validated_data)


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


class EventCreateSerializer(serializers.ModelSerializer):
    """
    EventSerializer class defines a
    serializer for handling serialization
    and deserialization of event data.
    """

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
                  )