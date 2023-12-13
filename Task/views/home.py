from django.shortcuts import render
from django.shortcuts import redirect
from Task.models import User
from Task.models import Category
from Task.models import Task
from django.contrib.auth.decorators import user_passes_test, login_required


@login_required
def home(request):   
    
        user = request.user
        tasks = Task.objects.filter(user = request.user)

        return render(request, './home.html', {
            'user': user,
            'tasks': tasks
        })
    
    