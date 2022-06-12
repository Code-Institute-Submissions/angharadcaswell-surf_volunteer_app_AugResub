from django.shortcuts import render
from django.views import generic, View
from volunteer_app.models import VolunteerProfile, Session


class VolunteerList(generic.ListView):
    template_name = 'dashboard.html'
    queryset = VolunteerProfile.objects.all()

class SessionList(generic.ListView):
    template_name = 'dashboard.html'
    queryset = Session().objects.all()



