from django.contrib import admin
from .models import User, Community_load, Research_load, Teaching_load

class Users(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email','teaching', 'administrative', 'research', 'community', 'load', 'total_load')
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
    list_display = ('user_id','activity', 'proof_community')
    list_filter = ('user_id',)
    search_fields = ('user_id',)

    class Meta:
        model = Community_load
admin.site.register(Community_load, Community)


# class Overall_Load(admin.ModelAdmin):
#     list_display = ('user_id','load', 'total_load')
#     list_filter = ('user_id',)
#     search_fields = ('user_id',)

#     class Meta:
#         model = Overall_load
# admin.site.register(Overall_load, Overall_Load)
