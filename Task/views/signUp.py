from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from Task.models import User
from django.contrib.auth import login
from django.db import IntegrityError
from django.contrib import messages


def signUp(request):
    if request.method == 'POST':
        if (request.POST.get('name')
                and request.POST.get('lastName')
                and request.POST.get('username')
                and request.POST.get('email')
                and request.POST.get('password1')
                and request.POST.get('password2')):
            if request.POST['password1'] == request.POST['password2']:
                try:
                    user = User.objects.create_user(first_name=request.POST['name'], password=request.POST['password1'],
                                                    email=request.POST['email'], is_active=True, is_staff=False,
                                                    is_superuser=False, 
                                                    last_name=request.POST['lastName'], username=request.POST['username'])
                    user.save()
                    login(request, user)
                    messages.success(request, 'Cuenta creada satisfactoriamente! (espera a que sea activada)')
                    return redirect('signin')
                except IntegrityError:
                    messages.error(request,"Usuario ya existe")
                    return render(request, 'signup.html')
            messages.error(request,"Contraseñas son distintas")
            return render(request, 'signup.html')
        else:
            messages.error(request,"Todos los campos son requeridos")
            return render(request, 'signup.html', {
                'form': UserCreationForm
            })
    else:
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })