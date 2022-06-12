from django.urls import path
from .views import VolunteerList

urlpatterns = [
    path('', VolunteerList.as_view(), name='dashboard'),

]