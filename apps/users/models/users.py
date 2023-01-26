"""User model."""

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

# Utilities
from apps.utils.models import TimeStampedModel


class User(TimeStampedModel, AbstractUser):
    """User model.

    Extend from Django's Abstract User, change the username field
    to email to make it unique.
    The required fields are now username, first_name.
    The field phone_number is formatted by means of regular expressions.
    The new field is created is_client.
    The new field is created and by default is_verfied is set to
    false until it is verified by mail, in development it is shown
    in console-log(cli) and in production you have to send an email.
    """

    email = models.EmailField(
        _("email address"),
        db_index=True,
        max_length=255,
        unique=True,
        error_messages={"unique": _("A user with that email already exists.")},
    )

    phone_regex = RegexValidator(
        regex=r"^\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$",
        message=_("Phone number must be entered in the format: +00 (000) 000-0000"),
    )

    phone_number = models.CharField(validators=[phone_regex], max_length=20, blank=True, null=True)

    # https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#django.contrib.auth.models.CustomUser.USERNAME_FIELD
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name"]

    is_public = models.BooleanField(
        default=True, help_text=_("Public profiles show all information about users.")
    )

    is_verified = models.BooleanField(
        _("verified"),
        default=False,
        help_text=_(
            "Determine if an user has a verified account. "
            "Set to true when user verified its email address."
        ),
    )

    is_client = models.BooleanField(
        "client",
        default=True,
        help_text=(
            "Help easily distinguish users and perform queries. "
            "Clients are the main type of user."
        ),
    )

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

    def __str__(self):
        """Return username."""
        return self.username

    # https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#django.contrib.auth.models.CustomUser.get_short_name
    def get_short_name(self):
        """Function is overwritten and return username. Instead of first_name"""
        return self.username

    @property
    def get_full_name(self):
        """Property for return full name."""
        return f"{self.first_name.title()} {self.last_name.title()}"


