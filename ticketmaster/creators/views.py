from rest_framework import generics
from ticketmaster.creators.models import Creators
from ticketmaster.creators.serializer import CreatorsSerializer

"""
this module define the views for events/reservations creators
"""


class CreatorsList(generics.ListCreateAPIView):
    """
    CreatorsList class defines an API endpoint for handling HTTP GET requests to list existing
    event/reservations creators and HTTP POST requests to create new creators.
    """
    queryset = Creators.objects.all()
    serializer_class = CreatorsSerializer


class CreatorsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    CreatorsDetail class defines an API endpoint for handling HTTP GET  PUT, and DELETE requests
    on a single creator instance
    """
    queryset = Creators.objects.all()
    serializer_class = CreatorsSerializer