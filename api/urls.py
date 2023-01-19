from django.urls import include, path, re_path
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api.users.urls import urlpatterns as users_urls

schema_view = get_schema_view(
    openapi.Info(
        title="Name API",
        default_version="v1",
        description="API endpoints for the api",
        terms_of_service="https://opensource.org/licenses/MIT",
        contact=openapi.Contact(email="nomackayu@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    url="http://localhost:8080/",
    public=True,
    permission_classes=(),
    authentication_classes=(),
)

"""
If the urs's of dj_rest_auth are active(auth/ & registration) in API,
then the urls of django-allauth are not active(accounts/) in templating

TODO: Check if it is possible to work both at the same time.
"""

urlpatterns = [
    path("", include(users_urls)),
    path("reg/", include("dj_rest_auth.registration.urls")),
    path("auth/", include("dj_rest_auth.urls")),
    # path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    re_path(r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    re_path(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
