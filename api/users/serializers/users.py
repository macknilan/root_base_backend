"""Serializer User"""

# Django REST Framework
from rest_framework import serializers

# Models
from apps.users.models import User, Profile

# Serializers
from api.users.serializers.profiles import ProfileModelSerializer


class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer."""

    class Meta:
        """Meta class."""
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "phone_number"
        )


class UserProfileModelSerializer(serializers.ModelSerializer):
    """User model serializer with profile model."""

    profile = ProfileModelSerializer(read_only=True)

    class Meta:
        """Meta class."""
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "profile"
        )


class DetailUserSerializer(serializers.Serializer):
    """Serializer detail user"""

    id = serializers.IntegerField(required=True)

    def validate_id(self, data):
        """Verify if the -id- exist"""

        try:
            User.objects.get(pk=data)
        except User.DoesNotExist:
            raise serializers.ValidationError('User does not exist (≖᷆︵︣≖)')

        return data

