from django.shortcuts import render
from django.shortcuts import redirect
from Task.models import User
from Task.models import Category
from Task.models import Task
import Task.forms as forms
from django.contrib.auth.decorators import user_passes_test, login_required


@login_required
def home(request):   
    if(request.method == 'GET'):
        user = request.user
        tasks = Task.objects.filter(user = request.user)
        opposite = request.session.get('opposite','Dark mode')

        return render(request, './home.html', {
            'user': user,
            'tasks': tasks,
            'filter': forms.basicFilters,
            'opposite': opposite
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
    
    