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
    """ Add session """ 
    if request.method == 'POST':
        form = SessionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # messages.success(request, f'You have successfully created session')
            return redirect('volunteer_dashboard')
        else:
            messages.error(
                request,
                'Please ensure all fields are filled out correctly.'
                )

    return render(request, 'add_sessions.html', {})


