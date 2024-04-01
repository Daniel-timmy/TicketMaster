from django.contrib import admin
from .models import Event, EventBooking


class EventsBookingInline(admin.TabularInline):
    model = EventBooking


class EventAdmin(admin.ModelAdmin):
    inlines = [
        EventsBookingInline,
    ]
    list_display = (
        'id',
        'event_name',
        'ticket_data',
        'start_date',
        'creator',
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


# Register your models here.
admin.site.register(Event, EventAdmin)
