from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('teaching_load', views.teaching_load, name='teaching_load'),
    path('research_load', views.research_load, name='research_load'),
    path('admin_load', views.admin_load, name='admin_load'),
    path('community_load', views.community_load, name='community_load'),
    path('profile', views.profile, name='profile'),
]
