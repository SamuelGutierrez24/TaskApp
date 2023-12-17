from django.shortcuts import render
from django.shortcuts import redirect
from Task.forms import taskCreationForm
from Task.forms import extraDataForm
from Task.models import ExtraData

def createTasks(request):   
    if request.method == 'GET':
        
        opposite = request.session.get('opposite', 'Dark mode')
        
        return render(request, './createTasks.html', {
            'taskForm': taskCreationForm,
            'extraData': extraDataForm,
            'user': request.user,
            'opposite':opposite           
        })
    else:
        print("Aaaaaaaaaaa", request.POST.get('opposite'))
        if request.POST.get('opposite') is not None:
            newMode = request.session.get('opposite', 'Dark mode')
            if(newMode == 'Dark mode'):
                request.session['opposite'] = 'Light mode'
            else:
                request.session['opposite'] = 'Dark mode'
                
            opposite = request.session.get('opposite', 'Dark mode')
            return render(request, './createTasks.html', {
            'taskForm': taskCreationForm,
            'extraData': extraDataForm,
            'user': request.user,
            'opposite':opposite        
        })
        else:
            form = taskCreationForm(request.POST)
            print('aaaaaaaaaaaa', form.errors)
            print('pipipipipipi', request.POST.get('taskDescription'))
            task = form.save(commit=False)
            task.user = request.user  # Asigna el usuario actual a la tarea
            task.save()
            nameList = request.POST.getlist('name')
            descList = request.POST.getlist('description')
            archive = request.POST.getlist('archive')
            if(request.POST.get('isExtra')=='True'):
                for n in range(len(nameList)):
                    if(nameList[n] != ''):
                        ExtraData.objects.create(nameExtra=nameList[n], contentExtra=descList[n],archive=archive[n],  task = task).save()
                
                
            return redirect('home') 