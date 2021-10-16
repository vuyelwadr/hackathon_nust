from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import auth
import requests


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


def teaching_load(request):
    if request.user.is_authenticated:
        userid =  request.user.id
        if request.method == 'POST':
            if 'courses' in request.POST:
                course_name = request.POST['course_name']
                coordinating = request.POST['coordinating']
                experience = request.POST['experience']
                sessions = request.POST['sessions']
                groups = request.POST['groups']

                course =  Courses.objects.create(user_id=userid, course_name=course_name, coordinating=coordinating, experience=experience, sessions=sessions, groups=groups)
                
            elif 'research_supervision' in request.POST:
                student_name = request.POST['student_name']
                research_type = request.POST['research_type']

                research_supervision = Research_supervision.create(user_id=user_id, student_name=student_name,  research_type=research_type)
                
        return render(request, 'teaching_load.html')
    else:
        return render(request, 'login.html')

