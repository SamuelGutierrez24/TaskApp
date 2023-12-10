from django.shortcuts import render
from django.shortcuts import redirect
from Task.forms import taskCreationForm
from Task.forms import extraDataForm

def createTasks(request):   
    if request.method == 'GET':
        return render(request, './createTasks.html', {
            'taskForm': taskCreationForm,
            'extraData': extraDataForm            
        })
    else:
        form = taskCreationForm(request.POST)
        form.save()
        return redirect('home')