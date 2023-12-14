from django.shortcuts import render
from django.shortcuts import redirect
from Task.models import Task
from Task.models import ExtraData

def taskDetails(request, tID):   
    task = Task.objects.get(id=tID)
    extra = ExtraData.objects.filter(task = task)
    isExtra = len(extra)>0
    return render(request, './taskDetails.html',{
        'task':task,
        'isExtra':isExtra,
        'extra':extra
    })