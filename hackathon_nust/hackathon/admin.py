from django.contrib import admin
from .models import User, Community_load, Research_load, Teaching_load, Admin_load, Courses, Research_project, Research_supervision
from django.contrib import messages
from django.apps import apps

administrative_weighing = 1

class Users(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','teaching', 'administrative', 'research', 'community', 'load', 'total_load')
    list_filter = ('load','total_load')
    search_fields = ('id',)

    class Meta:
        model = User
admin.site.register(User, Users)


# Register your models here.
class Teaching(admin.ModelAdmin):
    #show the following in the admin screen
    list_display = ('user_id','courses', 'honours_research_supervision' )
    # allow the admin to filter using the following fields
    list_filter = ('user_id',)
    # allow the admin to search using the following fields
    search_fields = ('user_id',)

    class Meta:
        # define the model to pull data from
        model = Teaching_load
        
#show data from the Teaching_load table using the formatting defined by the Teaching class
admin.site.register(Teaching_load, Teaching)

class Research(admin.ModelAdmin):
    list_display = ('user_id','research_projects', 'postgraduate_research_supervision' )
    list_filter = ('user_id',)
    search_fields = ('user_id',)

    class Meta:
        model = Research_load
        
admin.site.register(Research_load, Research)

class Community(admin.ModelAdmin):
    change_form_template = "admin_pannel_addons.html"
    list_display = ('user_id','activity', 'proof_community', 'status')
    list_filter = ('user_id', 'status')
    search_fields = ('user_id',)

    class Meta:
        model = Community_load

    def response_change(self, request, obj):
        object_id = request.resolver_match.kwargs['object_id']
        
        if "Approve" in request.POST:
            userid = request.POST['user']
            Community_load.objects.filter(id=userid).update(status="Approved")
            return super(Requests, self).response_change(request, obj)
        elif "Deny" in request.POST:
            user_id = request.POST['user']
            Community_load.objects.filter(id=userid).update(status="Rejected")
            return super(Requests, self).response_change(request, obj)
        else:
            return super(Requests, self).response_change(request, obj)
admin.site.register(Community_load, Community)


class Administrative_load(admin.ModelAdmin):
    list_display = ('user_id','duties')
    list_filter = ('duties',)
    search_fields = ('user_id',)

    class Meta:
        model = Community_load
    

    def save_model(self, request, obj, form, change):
        if 'duties' in form.changed_data:
            user_id = request.POST['user']

            detail = User.objects.prefetch_related().get(id=user_id)
            total_administrative_load = detail.administrative + administrative_weighing
            User.objects.filter(id=user_id).update(administrative = total_administrative_load)
            update_load(request, user_id)
        super(Administrative_load, self).save_model(request, obj, form, change)

admin.site.register(Admin_load, Administrative_load)


class Course(admin.ModelAdmin):
    list_display = ('user_id','course_name','coordinating', 'experience', 'sessions', 'groups')
    list_filter = ('user_id','coordinating')
    search_fields = ('user_id',)

    class Meta:
        model = Courses
admin.site.register(Courses, Course)


class Research_proj(admin.ModelAdmin):
    change_form_template = "admin_pannel_addons.html"
    list_display = ('id', 'project_name', 'proof_research', 'status' )
    list_filter = ('user_id', 'status')
    search_fields = ('user_id',)

    class Meta:
        model = Research_project
        
admin.site.register(Research_project, Research_proj)


class Research_sup(admin.ModelAdmin):
    change_form_template = "user_requests.html"
    list_display = ('user_id','student_name','research_type')
    list_filter = ('user_id',)
    search_fields = ('user_id',)
    
    class Meta:
        model = Research_supervision
admin.site.register(Research_supervision, Research_sup)









def update_load(request, userid):
    userid = userid
    user = User.objects.prefetch_related().get(id=userid)
    total_load = user.teaching + user.administrative + user.research + user.community
    User.objects.filter(id=userid).update(total_load=total_load)

    if total_load>=20:
        User.objects.filter(id=userid).update(load="h")
    elif total_load>10 and total_load<20:
        User.objects.filter(id=userid).update(load="m")
    else:
        User.objects.filter(id=userid).update(load="l")
 
