from django.contrib import admin

# Register your models here.
class teaching_load(admin.ModelAdmin):
     list_display = ('user_id','courses' )
     list_filter = ()
     search_fields = ()