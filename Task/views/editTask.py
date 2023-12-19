from django.shortcuts import render
from django.shortcuts import redirect
from Task.models import Task
from Task.forms import taskCreationForm
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, get_object_or_404



@login_required
def editTask(request, task_id):   
    task = get_object_or_404(Task, id=task_id)

    opposite = request.session.get('opposite', 'Dark mode')
    if request.method == 'POST':
        if request.POST.get('opposite') is None:
            return saveToDB(request, task_id)
        else:
            return manageDarkMode(request, task_id)
    else:
        form = taskCreationForm(instance=task)

        return render(request, 'editTask.html', {
            'task': task,
            'form': form,
            'opposite': opposite
        })
        

def manageDarkMode(request, task_id):
    
    task = get_object_or_404(Task, id=task_id)
    form = taskCreationForm(request.POST, instance=task)
    newMode = request.session.get('opposite', 'Dark mode')
    
    if(newMode == 'Dark mode'):
        request.session['opposite'] = 'Light mode'
    else:
        request.session['opposite'] = 'Dark mode'
        
    opposite = request.session.get('opposite', 'Dark mode')
    
    return render(request, 'editTask.html', {
            'task': task,
            'form': form,
            'opposite': opposite
        })

def saveToDB(request, task_id):
    opposite = request.session.get('opposite', 'Dark mode')
    task = get_object_or_404(Task, id=task_id)
    
    if 'delete_task' in request.POST:
        task.delete()
        return redirect('home')

    form = taskCreationForm(request.POST, instance=task)
    if form.is_valid():
        form.save()
        return redirect('home')