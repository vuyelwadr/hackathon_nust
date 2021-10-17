from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import auth
import requests
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from .models import Teaching_load, Research_supervision, Courses, Research_load, Research_project, Admin_load, Community_load, User


honours_research_weighting = 2
postgraduate_research_weighting = 1
course_weighting = 4
course_coordinating_weighing = 1
course_experience_fto_weighing = 2
course_experience_fti_weighing = 1
course_session_t_weighting = 1
course_session_p_weighting = 2
research_project_weighting = 4
community_activity_weighing = 2
administrative_weighing = 1

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
        return render(request, 'dashboard.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')


def teaching_load(request):
    if request.user.is_authenticated:
        try:
            userid = request.user.id
            teaching_load = Teaching_load.objects.prefetch_related().get(id=userid)
            research_load = Research_load.objects.prefetch_related().get(id=userid)
            user = User.objects.prefetch_related().get(id=userid)
            if request.method == 'POST':
                if 'courses' in request.POST:
                    course_name = request.POST['course_name']
                    coordinating = request.POST['coordinating']
                    experience = request.POST['experience']
                    sessions = request.POST['sessions']
                    groups = request.POST['groups']

                    # add values form courses table to Courses table 
                    course = Courses.objects.create(user_id=userid, course_name=course_name, coordinating=coordinating, experience=experience, sessions=sessions, groups=groups)

                    # set course loads
                    course_load = course_weighting

                    if coordinating:
                        course_load += course_coordinating_weighing

                    if experience=="1st_time_teaching_course_overall":
                        course_load += course_experience_fto_weighing
                    elif experience=="1st_time_teaching_course_at_institution":
                        course_load += course_experience_fti_weighing

                    if sessions=="theory":
                        course_load += course_session_t_weighting
                    elif sessions=="practical":
                        course_load += course_session_p_weighting

                    if int(groups)>0:
                        course_load += int(groups)

                    # Add calculated course load to current course load and overall teaching load
                    total_course_load = course_load + teaching_load.courses
                    total_teaching_load = user.teaching + course_load
                    
                    Teaching_load.objects.filter(id=userid).update(courses = total_course_load)
                    User.objects.filter(id=userid).update(teaching = total_teaching_load)

                    update_load(request)
                    
                elif 'research_supervision' in request.POST:
                    student_name = request.POST['student_name']
                    research_type = request.POST['research_type']

                    Research_supervision.objects.create(user_id=userid, student_name=student_name,  research_type=research_type)
                    
                    if research_type=="honours":
                        researchload = teaching_load.honours_research_supervision + honours_research_weighting
                        total_teaching_load = user.teaching + honours_research_weighting
                        Teaching_load.objects.filter(id=userid).update(honours_research_supervision = researchload)
                        User.objects.filter(id=userid).update(teaching = total_teaching_load)


                    elif research_type=="postgraduate":
                        researchload = research_load.postgraduate_research_supervision + postgraduate_research_weighting
                        total_research_load = user.research + postgraduate_research_weighting
                        Research_load.objects.filter(id=userid).update(postgraduate_research_supervision=researchload)
                        User.objects.filter(id=userid).update(research = total_research_load)

                    update_load(request)
                    messages.success(request,"Request Completed")

        except:
            messages.error(request,"Request Failed")
                    
        return render(request, 'teaching_load.html')
    else:
        return render(request, 'login.html')


def research_load(request):
    if request.user.is_authenticated:
        try:
            userid = request.user.id
            research_load = Research_load.objects.prefetch_related().get(id=userid)
            user = User.objects.prefetch_related().get(id=userid)
            if request.method == 'POST':
                    if 'project' in request.POST:
                        project_name = request.POST['project_name']
                        proof_research = request.FILES['proof_research']

                        researchload = research_load.research_projects + research_project_weighting
                        total_research_load = user.research + research_project_weighting
                        Research_project.objects.create(user_id=userid, project_name=project_name,  proof_research=proof_research)
                        Research_load.objects.filter(id=userid).update(research_projects = researchload)
                        User.objects.filter(id=userid).update(research = total_research_load)

                    elif 'research_supervision' in request.POST:
                        student_name = request.POST['student_name']
                        research_type = request.POST['research_type']

                        Research_supervision.objects.create(user_id=userid, student_name=student_name,  research_type=research_type)
                        
                        if research_type=="honours":
                            researchload = teaching_load.honours_research_supervision + honours_research_weighting
                            total_teaching_load = user.teaching + honours_research_weighting
                            Teaching_load.objects.filter(id=userid).update(honours_research_supervision = researchload)
                            User.objects.filter(id=userid).update(teaching = total_teaching_load)

                        elif research_type=="postgraduate":
                            researchload = research_load.postgraduate_research_supervision + postgraduate_research_weighting
                            total_research_load = user.research + postgraduate_research_weighting
                            Research_load.objects.filter(id=userid).update(postgraduate_research_supervision=researchload)
                            User.objects.filter(id=userid).update(research = total_research_load)
                    
                    update_load(request)
                    messages.success(request,"Request Completed")


            return render(request, 'research_load.html')
        except:
            messages.error(request,"Request Failed")
    else:
        return render(request, 'login.html')

#maybe just for viewing
def admin_load(request):
    return render(request, 'admin_load.html')

def community_load(request):
    if request.user.is_authenticated:

        userid = request.user.id
        research_load = Research_load.objects.prefetch_related().get(id=userid)
        user = User.objects.prefetch_related().get(id=userid)
        if request.method == 'POST':
            activity = request.POST['activity']
            proof_community = request.FILES['proof_community']

            total_community_load = user.community + community_activity_weighing
            Community_load.objects.create(user_id=userid, activity=activity,  proof_community=proof_community)
            User.objects.filter(id=userid).update(community = total_community_load)

            update_load(request)
            messages.success(request,"Request Completed")



        return render(request, 'community_load.html')
    else:
        return render(request, 'login.html')



def profile(request):
    if request.user.is_authenticated:
        userid = request.user.id
        update_load(request)
        user = User.objects.prefetch_related().get(id=userid)
        teaching_load = Teaching_load.objects.prefetch_related().get(id=userid)
        research_supervision = Research_supervision.objects.prefetch_related().get(id=userid)
        courses = Courses.objects.prefetch_related().get(id=userid)
        research_load = Research_load.objects.prefetch_related().get(id=userid)
        # research_project = Research_project.objects.prefetch_related().get(id=userid)
        # admin_load = Admin_load.objects.prefetch_related().get(id=userid)
        # Community_load = Community_load.objects.prefetch_related().get(id=userid)

        details = {'user':user, 'teaching_load':teaching_load, 'research_supervision':research_supervision, 'courses':courses, 'research_load':research_load }

    return render(request, 'profile.html', details)

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

def update_load(request):
    userid = request.user.id
    user = User.objects.prefetch_related().get(id=userid)
    total_load = user.teaching + user.administrative + user.research + user.community
    User.objects.filter(id=userid).update(total_load=total_load)

    if total_load>=20:
        User.objects.filter(id=userid).update(load="h")
    elif total_load>10 and total_load<20:
        User.objects.filter(id=userid).update(load="m")
    else:
        User.objects.filter(id=userid).update(load="l")
