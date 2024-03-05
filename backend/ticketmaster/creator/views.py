from rest_framework import generics
from .models import Creator
from .serializer import CreatorSerializer

"""
this module define the views for events/reservations creators
"""


class CreatorList(generics.ListCreateAPIView):
    """
    CreatorsList class defines an API endpoint for handling HTTP GET requests to list existing
    event/reservations creators and HTTP POST requests to create new creators.
    """
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer


class CreatorDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    CreatorsDetail class defines an API endpoint for handling HTTP GET  PUT, and DELETE requests
    on a single creator instance
    """
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer
