from django.urls import path
from .views import ReservationList, ReservationBookingDetail, ReservationBookingCreate, ReservationBookingList, \
    ReservationDetail

"""
This module defines url path for the reservations models
"""


urlpatterns = [
    path('', ReservationList.as_view(), name='reservation-list'),
    path('<int:pk>/', ReservationDetail.as_view(), name='reservation-detail'),
    path('bookings/', ReservationBookingList.as_view(), name='reservation-booking-list'),
    path('bookings/create/', ReservationBookingCreate.as_view(), name='reservation-booking-create'),
    path('bookings/<int:pk>/', ReservationBookingDetail.as_view(), name='reservation-booking-detail'),
]