from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import VolunteerProfile, Session
from .forms import SessionForm, ProfileForm, UpdateUserForm
from django.contrib import messages
from django.urls import reverse_lazy
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

    return render(request, 'add_sessions.html', {'form': SessionForm})


@login_required
def profile(request):
    VolunteerProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES,
                                   instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', {'user_form': user_form,
                                            'profile_form': profile_form})


class DeleteSession(generic.DeleteView):
    model = Session
    success_url = reverse_lazy('dashboard')
    success_message = "Session successfully deleted!"
    template_name = "session_confirm_delete.html"
