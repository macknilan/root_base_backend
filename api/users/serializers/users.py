"""Serializer User"""

# Django REST Framework
from rest_framework import serializers

# Models
from apps.users.models import User, Profile

# Serializers
from api.users.serializers.profiles import ProfileModelSerializer

PHONE_FORMAT = "+00 (000) 000-0000"


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

        if User.objects.filter(pk=data).exists():
            return data
        else:
            raise serializers.ValidationError('User does not exist (≖᷆︵︣≖)')


class UpdateUserSerializer(serializers.Serializer):
    """
    Serializer to update fields of user
    """
    first_name = serializers.CharField(min_length=6, max_length=150, required=True, help_text="Nombre")
    last_name = serializers.CharField(min_length=6, max_length=150, required=False, help_text="Apellido")
    phone_number = serializers.CharField(min_length=10, max_length=20, required=False, help_text=PHONE_FORMAT)
    biography = serializers.CharField(
        min_length=15,
        max_length=150,
        required=False,
        help_text="descripción del la persona"
    )
    picture = serializers.ImageField(
        max_length=20,
        required=False,
        help_text="Imagen del usuario",
        allow_empty_file=False,
        allow_null=False,
    )

    def validate_picture(self, data):
        """
        Validate if de image is less than 3MB
        :param data:
        :return: data
        """

        if data.size > 2 * 1024 * 1024:
            raise serializers.ValidationError("Image size should not be larger than 2mb")
        return data
