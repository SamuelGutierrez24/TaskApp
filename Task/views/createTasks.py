from django.shortcuts import render
from django.shortcuts import redirect
from Task.forms import taskCreationForm

def createTasks(request):   
    if request.method == 'GET':
        return render(request, './createTasks.html', {
            'taskForm': taskCreationForm
        })
    else:
        form = taskCreationForm(request.POST)
        form.save()
        return redirect('home')