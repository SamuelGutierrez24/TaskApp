from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TaskApp.settings')

# create a Celery instance and configure it using the settings from Django
celery_app = Celery('TaskApp')

# Load task modules from all registered Django app configs.
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks in all installed apps
celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    'revisar-tareas-diarias': {
        'task': 'TaskApp.tasks.send_reminder_emails',  # Ajusta esto con la ruta correcta a tu tarea
        'schedule': crontab(hour=2, minute=10),  # Programa la tarea a la 1 am todos los días
    },
}
CELERY_BROKER_URL = 'pyamqp://guest:guest@localhost:5672//'
