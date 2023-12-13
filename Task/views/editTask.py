from django.shortcuts import render
from django.shortcuts import redirect
from Task.models import Task
from Task.forms import taskCreationForm
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, get_object_or_404



@login_required
def editTask(request,task_id):   
    
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        form = taskCreationForm(request.POST, instance=task)
        if form.is_valid():
            form.save()  # Guarda los cambios en la tarea existente
            return redirect('home')  # Redirige a la página principal o donde desees después de editar
    else:
        # Si la solicitud es un GET, muestra el formulario con los datos actuales de la tarea
        form = taskCreationForm(instance=task)

    return render(request, 'editTask.html', {'form': form, 'task': task})  
    
    