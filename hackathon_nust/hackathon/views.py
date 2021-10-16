from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import auth


def index(request):
    return render(request,'login.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

