"""Ulrs Users"""

# Django
from django.urls import include, path

from .views import users as v

detail = {"get": "retrieve"}
upgrade = {"patch": "partial_update"}

urlpatterns = []

urlpatterns += [
    path(
        "users/<int:pk>/",
        v.UserDetailView.as_view({**detail}),
        name="detail-user",
    ),
    path(
        "users/update/",
        v.UserUpgradeView.as_view({**upgrade}),
        name="update-user",
    ),
]
