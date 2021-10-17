from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('teaching_load', views.teaching_load, name='teaching_load'),
    path('research_load', views.research_load, name='research_load'),
    path('community_load', views.community_load, name='community_load'),
    path('profile', views.profile, name='profile'),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
