from django.db import models
from django.conf import settings

# Django models here. (DATABASE TABLES)


class teaching_load(models.Model):
    # User will be a foreign key field. Models will be linked using a user_id field
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True)
    courses = models.IntegerField(default=0)
    honours_research_supervision = models.IntegerField(default=0)

class courses(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True)
    
    # define the types of sessions with first element in each tuple as the actual value to be set on the model, and the second element is the human-readable name
    session_types = [('t','theory'), ('p','practical')]
    expirience_types = [('fto','1st time teaching course'), ('fti','1st time teaching course at institution'),('exp','expirienced')]

    name = models.CharField(max_length=50)
    coordinating = models.BooleanField(default=False)
    expirience = models.CharField(max_length=3, choices= expirience_types)
    #We should inlude the nuance for first time teaching specifically at the institution,
    #  keeping in mind ofcourse that first_time=true automatically means true here
    sessions = models.CharField(max_length=1, choices=session_types)
    groups = models.IntegerField(default=0)

class research_load(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True)
    project = models.CharField(max_length=50)
    student = models.CharField(max_length=50)
    proof_reasearch = models.FileField(upload_to='proof/research/')

class admin_load(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True)

    duties = models.CharField(max_length=50)

class community_load(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True)

    activity = models.CharField(max_length=50)
    proof_community = models.FileField(upload_to='proof/community_outreach/')

