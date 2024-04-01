import uuid

from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import ArrayField

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
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    ticket_data = ArrayField(
        models.JSONField(), default=None)
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


class ReservationBooking(models.Model):
    """
    Class that defines the amount of bookings made by users on a
    particular reservation
    """
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, default=None)
    customer_name = models.CharField()
    email = models.EmailField(unique=True, default=None)
    group_name = models.CharField(default=None)
    space_name = models.CharField(default=None)
    qr_code = models.BinaryField(default=None)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    event_type = models.CharField()
