"""Profile model."""

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _
from traitlets import default

# Utilities
from apps.utils.models import TimeStampedModel


class Profile(TimeStampedModel):
    """Profile model.

    User profile data
    A profile holds a user's public data like biography, picture,
    """

    user = models.OneToOneField("users.User", on_delete=models.CASCADE)

    picture = models.ImageField(
        _("profile picture"),
        blank=True,
        max_length=100,
        null=True,
        upload_to="users_pictures/",
    )
    biography = models.TextField(
        _("About your profile"),
        blank=True,
        null=True,
        help_text=_("A small biography about the user"),
        max_length=500,
    )

    def __str__(self):
        """Return user's str representation."""
        return str(self.user)
