from django.shortcuts import render
from .forms import SignUpForms

# Create your views here.


def login(request):
    return render(request, 'account/login.html')


def registration(request):
    return render(request, 'account/registration.html')


def welcome(request):
    return render(request, 'account/welcome.html')


def logout(request):
    return render(request, 'account/logout.html')