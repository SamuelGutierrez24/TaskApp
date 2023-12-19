from django.shortcuts import render
from django.shortcuts import redirect
from Task.models import Task
from Task.models import ExtraData
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import get_object_or_404


@login_required
def taskDetails(request, tID):   
    if request.method == 'GET':
        task = get_object_or_404(Task, id=tID)
        extra = ExtraData.objects.filter(task = task)
        isExtra = len(extra)>0
        opposite = request.session.get('opposite', 'Dark mode')
        
        return render(request, './taskDetails.html',{
            'task':task,
            'isExtra':isExtra,
            'extra':extra,
            'opposite':opposite
        })
        
    else:
        return manageDarkMode(request, tID)
    
def manageDarkMode(request, tID):
    newMode = request.session.get('opposite', 'Dark mode')
    if(newMode == 'Dark mode'):
        request.session['opposite'] = 'Light mode'
    else:
        request.session['opposite'] = 'Dark mode'
        
    task = Task.objects.get(id=tID)
    extra = ExtraData.objects.filter(task = task)
    isExtra = len(extra)>0
    opposite = request.session.get('opposite', 'Dark mode')
    
    return render(request, './taskDetails.html',{
        'task':task,
        'isExtra':isExtra,
        'extra':extra,
        'opposite':opposite
    })