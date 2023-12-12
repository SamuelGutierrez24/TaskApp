from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def signin(request):
    logout(request)
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        login(request,user)
        return redirect('home')
