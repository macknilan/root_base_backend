"""
Vista MVC para listar un user junto con profile
"""
# Django
from django.db import IntegrityError, transaction

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.exceptions import APIException
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from shared.utils import ExepcionServidor, NotFoundSerializer

# Serializer
from api.users.serializers.users import (
    UserModelSerializer,
    DetailUserSerializer,
    UserProfileModelSerializer,
    UpdateUserSerializer
)

# Models
from apps.users.models import User, Profile


class UserDetailView(viewsets.GenericViewSet):
    """Get User

    Get user with profile.
    """
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: UserProfileModelSerializer(many=False),
            status.HTTP_404_NOT_FOUND: NotFoundSerializer(),
        },
    )
    @action(detail=True, methods=["get"])
    def retrieve(self, request, *args, **kwargs):
        """Get user & profile by id

        `
        """
        params = kwargs["pk"]
        serializer_params = DetailUserSerializer(data={"id": params})
        serializer_params.is_valid(raise_exception=True)
        try:
            qry_user = User.objects.get(pk=params)
        except ExepcionServidor as e:
            raise APIException(code=status.HTTP_400_BAD_REQUEST, detail=e.mensaje)
        serializer_response = UserProfileModelSerializer(qry_user, many=False)

        return Response(serializer_response.data, status=status.HTTP_200_OK)


class UserUpgradeView(viewsets.GenericViewSet):
    """Get User

    Get user with profile.
    """
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(
        request_body=UpdateUserSerializer,
        responses={
            status.HTTP_200_OK: UserProfileModelSerializer(many=False),
            status.HTTP_404_NOT_FOUND: NotFoundSerializer(),
        },
    )
    @action(detail=True, methods=["patch"])
    def partial_update(self, request, *args, **kwargs):
        """Update user

        Update user & profile went login catch ID
        """
        data_body = UpdateUserSerializer(data=request.data)
        if not data_body.is_valid():
            return Response(data_body.errors, status=status.HTTP_400_BAD_REQUEST)

        first_name = data_body.validated_data["first_name"]
        last_name = data_body.validated_data["last_name"]
        phone_number = data_body.validated_data["phone_number"]
        biography = data_body.validated_data["biography"]
        picture = data_body.validated_data["picture"]
        user_id = self.request.auth.payload.get("user_id")
        try:
            with transaction.atomic():
                User.objects.filter(id=user_id).update(
                    first_name=first_name,
                    last_name=last_name,
                    phone_number=phone_number
                )
                get_user_updated = User.objects.get(id=user_id)

                obj, upt_cre = Profile.objects.update_or_create(
                    user=get_user_updated,
                    defaults={
                        "biography": biography,
                        "picture": picture
                    },
                )
        except IntegrityError as error:
            raise APIException(code=status.HTTP_400_BAD_REQUEST, detail=error.__str__())

        try:
            qry_user = User.objects.get(pk=user_id)
        except ExepcionServidor as e:
            raise APIException(code=status.HTTP_400_BAD_REQUEST, detail=e.mensaje)
        serializer_response = UserProfileModelSerializer(qry_user, many=False)

        return Response(serializer_response.data, status=status.HTTP_200_OK)
