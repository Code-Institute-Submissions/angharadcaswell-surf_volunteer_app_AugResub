from django.shortcuts import render
from django.views import generic, View
from volunteer_app.models import VolunteerProfile, Session
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

    def edit_session_profile(request):
        session_form = forms.SessionForm()
        profile_form = forms.ProfileForm()
        if request.method == 'POST':
            if 'session_form' in request.POST:
                session_form = forms.SessionForm(request.POST)
                if session_form.is_valid():
                    session_form.save()
                    return redirect('home')
            if 'profile_form' in request.POST:
                profile_form = forms.ProfileForm(request.POST)
                if profile_form.is_valid():
                    profile_form.save()
                    return redirect('home')
        context = {
            'session_form': session_form,
            'profile_form': profile_form,
        }
        return render(request, 'add_session_profile.html', context=context)