import uuid

from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.postgres.fields import ArrayField
from backend.ticketmaster.creator.models import Creator
from creator.models import Creator
"""
Defines the model for reservations
"""


class Reservation(models.Model):
    """
    class that defines the reservation model:
    Suitable for applications used in managing car parking lots,
    working spaces and other places that have groups which have
    slots.
    """
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    reservation_name = models.CharField(max_length=100)
    groups = ArrayField(models.CharField(max_length=30, blank=True))
    spaces_per_group = ArrayField(models.CharField(max_length=10, blank=True))
    recurring_event = models.BooleanField()
    # TODO: replicate this on the customer's side
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()

    # TODO: multiple venues functionality
    venue_name = models.CharField(max_length=100)
    venue_address = models.CharField(max_length=1000)
    venue_country = models.CharField(max_length=100)
    online_event = models.BooleanField()
    description = models.CharField()

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.UUIDField()
    content_object = GenericForeignKey('content_type', 'object_id')


class ReservationBooking(models.Model):
    """
    Class that defines the amount of bookings made by users on a
    particular reservation
    """
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, default=None)
    customer_name = models.CharField()
    email = models.EmailField()
    alpha_numeric = models.CharField()
    QR_code = models.TextField()
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    event_type = models.CharField()
