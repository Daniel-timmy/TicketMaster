from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import Creator

"""
"""


class CreatorSerializer(serializers.ModelSerializer):
    """
    CreatorSerializer class defines a
    serializer for handling serialization
    and deserialization of creators data.
    """

    class Meta:
        model = Creator
        fields = (
            "id",
            "name",
            "company_name",
            "email",
            "password"
        )


class LoginCreatorSerializer(serializers.Serializer):
    """
     Serializer for creating a new login session.

    This serializer is used to validate and deserialize data when creating a new login session,
    typically in a login API endpoint. It expects the following input data:

    - username: A string representing the username or email of the user.
    - password: A string representing the password of the user.

    Example usage:
    ```
    {
        "username": "example_user",
        "password": "example_password"
    }
    ```

    Upon successful validation, this serializer can be used to authenticate the user and create a new session.
    """
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid details")
