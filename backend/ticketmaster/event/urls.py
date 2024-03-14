from django.urls import path
from .views import EventBookingDetail, EventList, EventBookingList, EventDetail, EventBookingCreate

"""
This module defines url path for the events models
"""

urlpatterns = [
    path('', EventList.as_view(), name='event-list'),
    path('<int:pk>/', EventDetail.as_view(), name='event-detail'),
    path('bookings/', EventBookingList.as_view(), name='event-booking-list'),
    path('bookings/create', EventBookingCreate.as_view(), name='event-booking-create'),
    path('bookings/<int:pk>', EventBookingDetail.as_view(), name='event-booking-detail'),
]