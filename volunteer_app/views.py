from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import FormView, CreateView
from .forms import ProfileForm
from .models import VolunteerProfile

# volunteer profile view
class EditProfile(CreateView):
    model= VolunteerProfile
    form_class= ProfileForm
    template_name= 'editprofile.html'
