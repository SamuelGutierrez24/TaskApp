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


@login_required
def home(request):   
    if(request.method == 'GET'):
        user = request.user
        tasks = Task.objects.filter(user = request.user)
        opposite = request.session.get('opposite','Dark mode')
        notis = Task.objects.filter(
        dueDate__range=[
            timezone.now(),
            timezone.now() + timezone.timedelta(days=3)
        ]
    )
        print('hola')
        print(notis)
        return render(request, './home.html', {
            'user': user,
            'tasks': tasks,
            'filter': forms.basicFilters,
            'opposite': opposite,
            'notis':notis
        })
    else:
        newMode = request.session.get('opposite', 'Dark mode')
        if(newMode == 'Dark mode'):
            request.session['opposite'] = 'Light mode'
        else:
            request.session['opposite'] = 'Dark mode'
        user = request.user
        tasks = Task.objects.filter(user = request.user)
        opposite = request.session.get('opposite','Dark mode')
        return render(request, './home.html', {
            'user': user,
            'tasks': tasks,
            'filter': forms.basicFilters,
            'opposite': opposite
        })
    


    
    