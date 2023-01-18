"""
Utilities file in shared folder to use in the whole project.
"""
from http import HTTPStatus
from typing import Any


# Django REST Framework
from rest_framework import status, serializers
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import exception_handler


class NotFoundSerializer(serializers.Serializer):
    """Serializador destinado solo para completar el Schema en Swagger"""

    detail = serializers.CharField(
        help_text="El mensaje de error"
    )


class ExepcionServidor(Exception):
    mensaje = "Excepción del servidor."

    def __init__(self):
        super().__init__(self.mensaje)

