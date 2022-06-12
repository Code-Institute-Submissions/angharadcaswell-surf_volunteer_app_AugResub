from django.urls import path
from .views import VolunteerList

urlpatterns = [
    path('', VolunteerList.as_view(), name='volunteer_list'),
    path('', SessionList.as_view(), name='session_list'),

]