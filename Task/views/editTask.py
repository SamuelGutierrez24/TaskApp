from django.shortcuts import render
from django.shortcuts import redirect
from Task.models import Task
from Task.forms import taskCreationForm
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, get_object_or_404



@login_required
def editTask(request, task_id):   
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        if 'delete_task' in request.POST:
            task.delete()
            return redirect('home')

        form = taskCreationForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = taskCreationForm(instance=task)

    return render(request, 'editTask.html', {
        'task': task,
        'form': form,
    })