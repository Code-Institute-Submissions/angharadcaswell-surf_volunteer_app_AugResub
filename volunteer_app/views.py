from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from .forms import ProfileForm
from .models import VolunteerProfile


#volunteer home view
class VolunteerPortfolio(generic.ListView):
    model = VolunteerProfile
    template_name = 'profile.html'


# edit volunteer profile view
class EditProfile(CreateView):
    model= VolunteerProfile
    form_class= ProfileForm
    template_name= 'editprofile.html'
