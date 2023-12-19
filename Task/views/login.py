from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect
from Task.models import User
from Task.models import Category
from Task.models import Task
import Task.forms as forms
from django.contrib.auth.decorators import user_passes_test, login_required
from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from Task.models import Task
from django.shortcuts import render
from django.shortcuts import redirect


def signin(request):
    logout(request)
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request,user)
            send_reminder_emails()
            return redirect('home')
        else:
            messages.error(request, "Usuario y/o contrasena incorrecta")
            return render(request, 'login.html')
        
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
    
    return tasks_to_remind