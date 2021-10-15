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
    session_types = [('t','theory'), ('p','theory')]

    name = models.CharField(max_length=50)
    coordinating = models.BooleanField(default=False)
    first_time = models.BooleanField(default=True)
    sessions = models.CharField(max_length=1, choices=session_types)
    groups = models.IntegerField(default=0)