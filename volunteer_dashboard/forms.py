from volunteer_app.models import Session, VolunteerProfile
from django import forms


class SessionForm(forms.ModelForm):

    class Meta:
        model = Session
        fields = ('date', 'time',)

class ProfileForm(forms.ModelForm):

    class Meta:
        model = VolunteerProfile
        fields = ('name', 'email', 'photo', 'bio')

        