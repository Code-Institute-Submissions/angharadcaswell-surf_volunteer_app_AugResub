from django.urls import path
from . import views
from .views import VolunteerList, profile

urlpatterns = [
    path('', VolunteerList.as_view(), name='dashboard'),
    path('add_sessions/', views.add_sessions, name='add_sessions'),
    path('profile/', profile, name='profile')
]