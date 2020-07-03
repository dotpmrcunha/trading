from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trading.settings')

app = Celery('trading')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = 'redis://0.0.0.0:6379/0'

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'add-new-symbol-information': {
        'task': 'app.tasks.add_daily_information',
        'schedule': 10.0
    },
}
