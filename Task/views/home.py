from django.shortcuts import render
from django.shortcuts import redirect
from Task.models import User
from Task.models import Category
from Task.models import Task
import Task.forms as forms
from django.contrib.auth.decorators import user_passes_test, login_required


@login_required
def home(request):   
    
    user = request.user
    tasks = Task.objects.filter(user = request.user)
    print(tasks.first().taskState)

    return render(request, './home.html', {
        'user': user,
        'tasks': tasks,
        'filter': forms.basicFilters
    })
    
    