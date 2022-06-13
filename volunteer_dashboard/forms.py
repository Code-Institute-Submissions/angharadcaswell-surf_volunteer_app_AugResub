from volunteer_app.models import Session, VolunteerProfile
from django import forms


class SessionForm(forms.ModelForm):
    session_form = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = Session
        fields = ('date', 'time',)

class ProfileForm(forms.ModelForm):
    profile_form = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = VolunteerProfile
        fields = ('name', 'email', 'bio')