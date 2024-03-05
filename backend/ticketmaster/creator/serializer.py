from rest_framework import serializers
from .models import Creator
# from ticketmaster.events.models import Events
# from .reservations.models import Reservations

"""
"""


class CreatorSerializer(serializers.ModelSerializer):
    """
    CreatorSerializer class defines a
    serializer for handling serialization
    and deserialization of creators data.
    """
    # events = serializers.PrimaryKeyRelatedField(
    #     many=True, queryset=Events.objects.all())

    # reservations = serializers.PrimaryKeyRelatedField(
    #     many=True, queryset=Reservations.objects.all()
    #     )

    class Meta:
        model = Creator
        fields = (
            "id",
            "name",
            "company_name",
            "email",
            "password"
        )
