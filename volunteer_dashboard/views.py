from django.shortcuts import render
from django.views import generic, View
from volunteer_app.models import VolunteerProfile, Session


class VolunteerList(generic.ListView):
    template_name = 'dashboard.html'
    context_object_name = 'volunteer_list'
    model = VolunteerProfile

    def get_queryset(self):
        return VolunteerProfile.objects.all()

    def get_context_data(self, **kwargs):
        context = super(VolunteerList, self).get_context_data(**kwargs)
        context['session_list'] = Session.objects.all()
        return context

    

# class SessionList(generic.ListView):
#     template_name = 'dashboard.html'
#     model = Session
#     queryset = Session.objects.all()
#     context_object_name = 'session_list'



