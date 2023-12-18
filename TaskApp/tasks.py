# tasks.py

from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from Task.models import Task
from django.shortcuts import render
from django.shortcuts import redirect

@shared_task
def send_reminder_emails():
    tasks_to_remind = Task.objects.filter(
        dueDate__range=[
            timezone.now(),
            timezone.now() + timezone.timedelta(days=3)
        ]
    )

    for task in tasks_to_remind:
        
        send_mail(
            f'Recordatorio: {task.taskName}',
            f'La tarea "{task.taskName}" está próxima a vencer el {task.dueDate}.',
            'settings.EMAIL_HOST_USER',
            [task.user.email],  
            fail_silently=False,
        )
