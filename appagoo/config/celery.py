# Stdlib imports
from __future__ import absolute_import
import os

# Core Django imports
from django.conf import settings

# Third-party app imports
from celery import Celery

# Appagoo imports
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Local')

from configurations import importer
importer.install()

app = Celery('config')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
