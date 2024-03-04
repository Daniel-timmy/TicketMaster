from django.urls import path
from .views import EventsBookingsDetail, EventsList

"""
This module defines url path for the events models
"""

urlpatterns = [
    path('events/', EventsList.as_view(), name='events-list'),
    path('event-bookings/<int:pk>/', EventsBookingsDetail.as_view(), name='event-bookings-detail'),
]