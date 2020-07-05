from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trading.settings')

app = Celery('trading')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'add-new-symbol-information': {
        'task': 'app.tasks.add_daily_information',
        'schedule': crontab(minute=0, hour=0, day_of_week=[2, 3, 4, 5, 6])
    },
}
