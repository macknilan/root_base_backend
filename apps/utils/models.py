# https://docs.djangoproject.com/en/4.1/topics/db/models/#model-inheritance

from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    """Time Stamped Model.

    This model act as abstract model and define fields that all others
    models in the application must to have.

    An abstract base class model that provides self-updating
    created and modified fields.
    """

    created = models.DateTimeField(
        _("created"),
        auto_now_add=True,
        help_text=_("Date time at which an object was created"),
    )
    modified = models.DateTimeField(
        _("modified"),
        auto_now=True,
        help_text=_("Date time at which an object was modified"),
    )

    class Meta:
        """Meta option."""

        # https://docs.djangoproject.com/en/4.1/ref/models/options/#available-meta-options
        abstract = True

        get_latest_by = "created"
        ordering = ["-created", "-modified"]
