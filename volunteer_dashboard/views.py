from django.shortcuts import render, redirect
from django.views import generic, View
from .models import VolunteerProfile, Session
from .forms import SessionForm, ProfileForm, UpdateUserForm
from django.contrib import messages
import PIL 
from PIL import Image
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

    
def add_sessions(request):
    if request.POST:
        form = SessionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('dashboard')
 
    return render(request, 'add_sessions.html', {'form' : SessionForm})

@login_required
def profile(request):
    VolunteerProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            # profile_form.instance.email = request.user.email
            # profile_form.name = request.user.username
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('dashboard')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', {'user_form': user_form,'profile_form' : ProfileForm})

