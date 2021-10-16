from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import auth
import requests
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from .models import Teaching_load, Research_supervision, Courses, Research_load, Research_project, Admin_load, Community_load, User

honours_research_weighting = 2

def index(request):
    if request.user.is_authenticated:
        update_load(request)
        return render(request, 'dashboard.html')
    else:
        return render(request,'login.html')

def dashboard(request):
    if request.user.is_authenticated:
        initialize(request)
        update_load(request)
        messages.info(request, "teach")
        return render(request, 'dashboard.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')


def teaching_load(request):
    if request.user.is_authenticated:
        userid = request.user.id
        teaching_load = Teaching_load.objects.prefetch_related().get(id=userid)
        user = User.objects.prefetch_related().get(id=userid)
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

                research_supervision = Research_supervision.objects.create(user_id=userid, student_name=student_name,  research_type=research_type)
                
                honoursload = teaching_load.honours_research_supervision + honours_research_weighting
                updated_teaching_load = honoursload + user.teaching

                teaching = Teaching_load(id=userid, user_id=userid, honours_research_supervision = honoursload)
                teaching.save()

                User.objects.filter(id=userid).update(teaching=updated_teaching_load)


                


                messages.info(request, honoursload)
                
        return render(request, 'teaching_load.html')
    else:
        return render(request, 'login.html')


def initialize(request):
    userid = request.user.id
    # try loading userdata from teaching_load and researchload, if no data then an exception will be thrown and the values will be initialized
    try:
        teaching_load = Teaching_load.objects.prefetch_related().get(id=userid)
        research_load = Research_load.objects.prefetch_related().get(id=userid)
    except:
        teaching = Teaching_load(id=userid, user_id=userid, courses=0, honours_research_supervision=0)
        research = Research_load(id=userid, user_id=userid, research_projects=0, postgraduate_research_supervision=0)
        teaching.save()
        research.save()
        messages.info(request, "teach")

def update_load(request):
    userid = request.user.id
    user = User.objects.prefetch_related().get(id=userid)
    total_load = user.teaching + user.administrative + user.research + user.community
    User.objects.filter(id=userid).update(total_load=total_load)

    if total_load<=5:
        User.objects.filter(id=userid).update(load="low")
    elif total_load>5 and total_load<10:
        User.objects.filter(id=userid).update(load="medium")
    elif total_load>10:
        User.objects.filter(id=userid).update(load="high")

