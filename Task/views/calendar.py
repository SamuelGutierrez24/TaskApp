from django.shortcuts import render
from django.shortcuts import redirect
from Task.models import Task

def calendar(request):   
    return render(request, './calendar.html', {
        'tasksList':Task.objects.all(),
        'tazk': Task.objects.first()
    })