from django.shortcuts import render
from django.shortcuts import redirect
from Task.models import Task

def calendar(request):  
    if(request.method == 'GET'):
        opposite = request.session.get('opposite','Dark mode')
        return render(request, './calendar.html', {
            'tasksList':Task.objects.filter(user = request.user),
            'tazk': Task.objects.first(),
            'opposite': opposite
        })
    else:
        newMode = request.session.get('opposite','Dark mode')
        if(newMode == 'Dark mode'):
            request.session['opposite'] = 'Light mode'
        else:
            request.session['opposite'] = 'Dark mode'
        opposite = request.session.get('opposite','Dark mode')
        return render(request, './calendar.html', {
            'tasksList':Task.objects.filter(user = request.user),
            'tazk': Task.objects.first(),
            'opposite': opposite
        })