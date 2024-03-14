from django.contrib import admin
from .models import Reservation, ReservationBooking


# Register your models here.

class ReservationBookingInline(admin.TabularInline):
    model = ReservationBooking


class ReservationAdmin(admin.ModelAdmin):
    inlines = [
        ReservationBookingInline,
    ]
    list_display = (
        "id",
        "reservation_name",
        "groups",
        "spaces_per_group",
        "recurring_event",
        "start_date",
        "start_time",
        "end_date",
        "end_time",
        "venue_name",
        "venue_address",
        "venue_country",
        "online_event",
        "description",
    )


admin.site.register(Reservation, ReservationAdmin)
