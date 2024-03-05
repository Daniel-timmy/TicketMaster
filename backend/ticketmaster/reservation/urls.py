from django.urls import path
from .views import ReservationList, ReservationBookingDetail

"""
This module defines url path for the reservations models
"""

urlpatterns = [
    path('/', ReservationList.as_view(), name='reservations-list'),
    path('bookings/<int:pk>/', ReservationBookingDetail.as_view(), name='reservation-bookings-detail'),
]