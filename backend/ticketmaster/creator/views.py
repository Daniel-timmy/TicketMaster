from knox.models import AuthToken
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import Creator
from .serializer import CreatorSerializer, LoginCreatorSerializer

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


class CreatorDetail(generics.RetrieveAPIView):
    """
    CreatorsDetail class defines an API endpoint for handling HTTP GET requests
    on a single creator instance
    """
    permission_classes = [IsAuthenticated,]
    serializer_class = CreatorSerializer

    def get_object(self):
        return self.request.user


class CreatorRegistration(generics.CreateAPIView):
    """
    CreatorRegistration class used to register a user and
    Specify the serializer class to use for validating and
    deserializing the request data
    """
    permission_classes = (AllowAny,)
    serializer_class = CreatorSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        print(user.email)
        return Response({
            'user': CreatorSerializer(user, context=self.get_serializer_context()).data,
            'token': AuthToken.objects.create(user)[1]
        })


class LoginAPI(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginCreatorSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": CreatorSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })
