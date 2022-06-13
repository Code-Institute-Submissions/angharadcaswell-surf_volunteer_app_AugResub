from django.shortcuts import render
from django.views import generic, View
from volunteer_app.models import VolunteerProfile, Session
from .forms import SessionForm
from django.contrib.auth.decorators import login_required


class VolunteerList(generic.ListView):
    template_name = 'dashboard.html'
    context_object_name = 'volunteer_list'
    model = VolunteerProfile

    def get_queryset(self):
        return VolunteerProfile.objects.all()

    def get_context_data(self, **kwargs):
        context = super(VolunteerList, self).get_context_data(**kwargs)
        context['session_list'] = Session.objects.order_by('date')
        return context



@login_required
def add_sessions(request):
    form = SessionForm(request.POST, request.FILES)
    print(request.FILES)
    return render(request, 'add_sessions.html', {'form' : form})


