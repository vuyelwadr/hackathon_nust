from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Django models here. (DATABASE TABLES)

class User(AbstractUser):
    load_types = [('h', 'high'), ('l', 'low'), ('m', 'medium')]

    load = models.CharField(max_length=1, choices=load_types, default='l')
    teaching = models.IntegerField(default=0)
    administrative = models.IntegerField(default=0)
    research = models.IntegerField(default=0)
    community = models.IntegerField(default=0)
    total_load = models.IntegerField(default=0)


class Teaching_load(models.Model):
    # User will be a foreign key field. Models will be linked using a user_id field
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True)
    courses = models.IntegerField(default=0)
    honours_research_supervision = models.IntegerField(default=0)

class Research_supervision(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True)
    
    research_types = [('h','honours'), ('p','postgraduate')]
    student_name = models.CharField(max_length=50)
    research_type = models.CharField(max_length=1, choices=research_types)

class Courses(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True)
    
    # define the types of sessions with first element in each tuple as the actual value to be set on the model, and the second element is the human-readable name
    session_types = [('t','theory'), ('p','practical')]
    experience_types = [('fto','1st_time_teaching_course_overall'), ('fti','1st_time_teaching_course_at_institution'),('exp','experienced')]

    course_name = models.CharField(max_length=50)
    coordinating = models.BooleanField(default=False)
    experience = models.CharField(max_length=3, choices= experience_types)
    sessions = models.CharField(max_length=1, choices=session_types)
    groups = models.IntegerField(default=0)

class Research_load(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True)
    research_projects = models.IntegerField(default=0)
    postgraduate_research_supervision = models.IntegerField(default=0)

class Research_project(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True)
    project_name = models.CharField(max_length=50)
    proof_research = models.FileField(upload_to='proof/research/')
    

class Admin_load(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True)

    duties = models.CharField(max_length=50)

class Community_load(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True)

    activity = models.CharField(max_length=50)
    proof_community = models.FileField(upload_to='proof/community_outreach/')
