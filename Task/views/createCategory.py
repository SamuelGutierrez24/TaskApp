from django.shortcuts import render
from django.shortcuts import redirect
from Task.forms import categoryCreationForm

def createCategory(request):   
    if request.method == 'GET':
        return render(request, './createCategory.html', {
            'taskForm': categoryCreationForm
        })
    else:
        form = categoryCreationForm(request.POST)
        form.save()
        return redirect('home')