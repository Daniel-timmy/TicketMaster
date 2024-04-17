import uuid
from datetime import datetime
import qrcode
from django.core.exceptions import ValidationError
from django.db import transaction
from psycopg2 import IntegrityError

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
    if not int(no_of_tickets) or no_of_tickets is None or int(no_of_tickets) <= 0:
        return []
    ticket_list = []

    for i in range(0, int(no_of_tickets)):
        t_data = {"ticket_id": str(uuid.uuid4()),
                  "available": True,
                  "attendee_id": None}
        ticket_list.append(t_data)
    return ticket_list


def generate_qr_code(data):
    if data is None or data == {}:
        return None
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


def update_first_available_ticket(instance, new_attendee_id):
    for ticket in instance.ticket_data:
        if ticket['attendee_id'] is None:
            ticket['attendee_id'] = new_attendee_id
            instance.save()
            return ticket
    raise ValueError('Tickets are no longer available')


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
                  'no_of_tickets',
                  'registration_end_date',
                  )

    def create(self, validated_data):
        """

        :param validated_data:
        :return:
        """

        no_of_tickets = validated_data.pop('no_of_tickets')
        total_cost = validated_data.pop('total_cost', None)
        if total_cost is None or total_cost <= 0:
            raise serializers.ValidationError("Total cost must be a positive number")
        if no_of_tickets is not None and no_of_tickets <= 0:
            raise serializers.ValidationError("Number of tickets must be a positive number")
        ticket_data = generate_ticket_data(no_of_tickets)
        if not ticket_data:
            raise ValueError("Number of ticket is invalid")
        validated_data['ticket_data'] = ticket_data
        if self.context['request'].user is None:
            raise ValidationError('User authentication failed')
        creator = get_user(self.context['request'])
        validated_data['creator'] = creator
        if validated_data['registration_end_date'] is None:
            validated_data['registration_end_date'] \
                = datetime.combine(date=validated_data['start_date'],
                                   time=validated_data['start_time'])
        try:
            instance = Event.objects.create(**validated_data)
            return instance
        except (ValidationError, IntegrityError, Exception) as e:
            print("Error: ", {e})
            raise


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
            'phone_number',
            'extra_info'
        )

    def create(self, validated_data):
        """

        :param validated_data:
        :return:
        """
        data_dict = validated_data.copy()
        qc = generate_qr_code(data_dict)
        if qc is None:
            raise ValueError('Wrong input data')
        data_dict['qr_code'] = qc
        data_dict['event'] = self.context['event']

        with transaction.atomic():
            try:
                ticket = update_first_available_ticket(instance=self.context['event'], new_attendee_id=data_dict['id'])
            except ValueError as e:
                return f"{e}"
            try:
                instance = EventBooking.objects.create(**data_dict)
            except (ValidationError, Exception):
                print("Event creation error")
            return instance, qc
