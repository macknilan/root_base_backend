"""
Instalación de celery #1
"""

import os

from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.local")

app = Celery("root_base_backend")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


# En __init__.py 👇
# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
# from .celery_app import app as celery_app

# __all__ = ("celery_app",)
