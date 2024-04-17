import uuid

from django.conf import settings
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
    ONLINE = 'ON'
    PHYSICAL = 'PH'
    BOTH = 'BO'

    EVENT_TYPES = [
        (ONLINE, 'Online'),
        (PHYSICAL, 'Physical'),
        (BOTH, 'Both'),
    ]
    DAILY = 'DY'
    WEEKLY = 'WK'
    MONTHLY = 'MN'
    ONE_TIME = 'OT'

    RECURRING_MODE = [
        (DAILY, 'Daily'),
        (WEEKLY, 'Weekly'),
        (MONTHLY, 'Monthly'),
        (ONE_TIME, 'One time')
    ]

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, default=None, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100)
    ticket_data = ArrayField(
        models.JSONField(), default=None)
    # if it happens to be a recurring the start and end date will
    # encompass the entire duration through which the event will keep
    # repeating. The start and end time will apply to each of the instance
    # the event will repeat
    start_date = models.DateField(default=None)
    start_time = models.TimeField(default=None)
    end_date = models.DateField(default=None)
    end_time = models.TimeField(default=None)
    venue_name = models.CharField(max_length=100)
    venue_address = models.CharField(max_length=1000)
    venue_country = models.CharField(max_length=100)
    online_event = models.CharField(
        max_length=2,
        choices=EVENT_TYPES,
        default=ONLINE,
    )
    recurring_event = models.CharField(
        max_length=2,
        choices=RECURRING_MODE,
        default=ONE_TIME,
    )
    description = models.TextField()
    registration_end_date = models.DateTimeField(null=True, blank=True)
    # featured(public, private)
    # theme/ custom flyer

    def __str__(self):
        return self.event_name


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
    phone_number = models.PositiveIntegerField(max_length=12)
    extra_info = ArrayField(
        models.JSONField(), default=[])
    # reminder options
