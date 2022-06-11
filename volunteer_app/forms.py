from django import forms
from .models import VolunteerProfile


class ProfileForm(forms.ModelForm):

    class Meta:
        model = VolunteerProfile
        fields = ('name', 'email', 'photo', 'bio')