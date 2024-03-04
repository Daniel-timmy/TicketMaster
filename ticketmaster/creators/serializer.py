from rest_framework import serializers
from ticketmaster.creators.models import Creators
from ticketmaster.events.models import Events
from ticketmaster.reservations.models import Reservations

"""
"""


class CreatorsSerializer(serializers.ModelSerializer):
    """
    CreatorsSerializer class defines a
    serializer for handling serialization
    and deserialization of creators data.
    """
    events = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Events.objects.all())

    reservations = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Reservations.objects.all()
        )

    class Meta:
        model = Creators
        fields = (
            "id",
            "name",
            "company_name",
            "email",
            "password"
        )
