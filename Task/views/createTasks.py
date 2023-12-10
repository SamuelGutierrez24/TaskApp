from django.shortcuts import render
from django.shortcuts import redirect
from Task.forms import taskCreationForm
from Task.forms import extraDataForm
from Task.models import ExtraData

def createTasks(request):   
    if request.method == 'GET':
        return render(request, './createTasks.html', {
            'taskForm': taskCreationForm,
            'extraData': extraDataForm            
        })
    else:
        form = taskCreationForm(request.POST)
        a = form.save()
        nameList = request.POST.getlist('name')
        descList = request.POST.getlist('description')
        
        
        #for n in range(len(nameList)):
            
        return redirect('home')