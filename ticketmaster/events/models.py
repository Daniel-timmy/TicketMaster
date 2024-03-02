from django.db import models
from django.contrib.postgres.fields import ArrayField

"""
Defines the model for events
"""


class Events(models.Model):
    """
    class that defines the events model:
    Suitable for applications such as an exclusive meeting,
    concerts, on-spot booking and the likes. Mainly ticketing.
    """
    # TODO: number of tickets
    event_name = models.CharField(max_length=100)
    tickets = ArrayField(models.CharField(max_length=512))
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    venue_name = models.CharField(max_length=100)
    venue_address = models.CharField(max_length=1000)
    venue_country = models.CharField(max_length=100)
    online_event = models.BooleanField()
    recurring_event = models.BooleanField()
    description = models.CharField()


class EventsBookings(models.Model):
    """
    Class that defines the amount of bookings made by users on a
    particular event.
    """
    customer_name = models.CharField()
    email = models.EmailField()
    alpha_numeric = models.CharField()
    QR_code = models.CharField()
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    event_type = models.CharField()
