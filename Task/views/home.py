from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
   
    if request.method == "GET":
        return render(request, 'home.html')
    else:
        return render(request, 'home.html')
