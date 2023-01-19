"""
Vista MVC para listar un user junto con profile
"""

# Django REST Framework
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import mixins, status, viewsets
from drf_yasg.utils import swagger_auto_schema
from shared.utils import ExepcionServidor, NotFoundSerializer

# Serializer
from api.users.serializers.users import UserModelSerializer, DetailUserSerializer, UserProfileModelSerializer

# Models
from apps.users.models import User


class UserView(viewsets.GenericViewSet):
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
        params = int(kwargs["pk"])
        srlz_params = DetailUserSerializer(data={"id": params})

        srlz_params.is_valid(raise_exception=True)
        try:
            qry_user = User.objects.get(pk=params)

        except ExepcionServidor as e:
            raise APIException(code=status.HTTP_400_BAD_REQUEST, detail=e.mensaje)
        srlz_response = UserProfileModelSerializer(qry_user, many=False)

        return Response(srlz_response.data, status=status.HTTP_200_OK)
