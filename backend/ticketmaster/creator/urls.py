from django.urls import path
from .views import LoginAPI, CreatorList, CreatorDetail, CreatorRegistration
from knox import views as knox_views
"""
This module defines url path for the events models
"""

urlpatterns = [
    path('', CreatorList.as_view(), name='creator-list'),
    path('login', LoginAPI.as_view(), name='creator-login'),
    path('logout', knox_views.LogoutView.as_view(), name='creator-logout'),
    path('user/', CreatorDetail.as_view(), name='creator-detail'),
    path('register/', CreatorRegistration.as_view(), name='registration')
]