from django.urls import path
from .views import CreatorList, CreatorDetail

"""
This module defines url path for the events models
"""

urlpatterns = [
    path('/', CreatorList.as_view(), name='creator-list'),
    path('/<int:pk>/', CreatorDetail.as_view(), name='creator-detail'),
]