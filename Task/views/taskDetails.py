from django.shortcuts import render
from django.shortcuts import redirect
from Task.models import Task

def taskDetails(request, tID):   
    task = Task.objects.get(id=tID)
    return render(request, './taskDetails.html',{
        'task':task
    })