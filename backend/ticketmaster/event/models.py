import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.postgres.fields import ArrayField
"""
Defines the model for event
"""


class Event(models.Model):
    """
    class that defines the events model:
    Suitable for applications such as an exclusive meeting,
    concerts, on-spot booking and the likes. Mainly ticketing.
    """
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    creator = models.ForeignKey(get_user_model(),default=None, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100)
    ticket_data = ArrayField(
        models.JSONField(), default=None)
    email = models.EmailField(unique=True, default=None)
    start_date = models.DateField(default=None)
    start_time = models.TimeField(default=None)
    end_date = models.DateField(default=None)
    end_time = models.TimeField(default=None)
    venue_name = models.CharField(max_length=100)
    venue_address = models.CharField(max_length=1000)
    venue_country = models.CharField(max_length=100)
    online_event = models.BooleanField()
    recurring_event = models.BooleanField()
    description = models.CharField()


class EventBooking(models.Model):
    """
    Class that defines the amount of bookings made by users on a
    particular event.
    """
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default=None)
    customer_name = models.CharField()
    email = models.EmailField(unique=True, default=None)
    qr_code = models.BinaryField(default=None)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    event_type = models.CharField()
