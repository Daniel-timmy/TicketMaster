from django.urls import path
from .views import EventBookingDetail, EventList

"""
This module defines url path for the events models
"""

urlpatterns = [
    path('/', EventList.as_view(), name='event-list'),
    path('bookings/<int:pk>/', EventBookingDetail.as_view(), name='event-booking-detail'),
]