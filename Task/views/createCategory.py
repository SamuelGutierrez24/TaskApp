from django.shortcuts import render
from django.shortcuts import redirect
from Task.forms import categoryCreationForm
from django.contrib.auth.decorators import user_passes_test, login_required

@login_required
def createCategory(request):   
    if request.method == 'GET':
        opposite = request.session.get('opposite', 'Dark mode')
        return render(request, './createCategory.html', {
            'taskForm': categoryCreationForm,
            'opposite': opposite
        })
    else:
        
        if(request.POST.get('opposite') is not None):
            return manageDarkMode(request)
        
        return saveToDB(request)

def manageDarkMode(request):
    
    newMode = request.session.get('opposite', 'Dark mode')
    if(newMode == 'Dark mode'):
        request.session['opposite'] = 'Light mode'
    else:
        request.session['opposite'] = 'Dark mode'
        
    opposite = request.session.get('opposite', 'Dark mode')
    
    return render(request, './createCategory.html', {
    'taskForm': categoryCreationForm,
    'opposite': opposite
    })


def saveToDB(request):
    
    form = categoryCreationForm(request.POST)
    category = form.save(commit=False)
    print(category)
    category.save()
    return redirect('home')