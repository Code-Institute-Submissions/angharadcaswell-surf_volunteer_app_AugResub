from django.shortcuts import render, redirect
from django.views import generic, View
from .models import VolunteerProfile, Session
from .forms import SessionForm



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

    
def add_sessions(request):
    if request.POST:
        form = SessionForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
        return redirect('dashboard')
 
    return render(request, 'add_sessions.html', {'form' : SessionForm})


