"""Ulrs Users"""

# Django
from django.urls import include, path

# Views
from api.users.views import users as v

detail_user = {"get": "retrieve"}

urlpatterns = []

urlpatterns += [
    path(
        "users/<int:pk>/",
        v.UserView.as_view({**detail_user}),
        name="user",
    ),
]
