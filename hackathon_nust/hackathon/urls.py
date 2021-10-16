from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('teaching_load', views.teaching_load, name='teaching_load'),
]
