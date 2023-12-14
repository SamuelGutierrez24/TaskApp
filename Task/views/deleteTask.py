from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, get_object_or_404
from Task.models import Task
from django.shortcuts import render
from django.shortcuts import redirect

@login_required
def deleteTask(request, task_id):   
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('home')
        