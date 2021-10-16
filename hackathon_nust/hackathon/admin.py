from django.contrib import admin
from .models import Teaching_load

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