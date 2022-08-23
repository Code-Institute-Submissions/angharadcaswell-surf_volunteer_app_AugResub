from .models import Session, VolunteerProfile
from django.contrib.auth.models import User
from django import forms


class DatePickerInput(forms.DateInput):
    input_type = 'date'


class TimePickerInput(forms.TimeInput):
    input_type = 'time'


class SessionForm(forms.ModelForm):
    date = forms.DateField(widget=DatePickerInput)
    time = forms.TimeField(widget=TimePickerInput)

    class Meta:
        model = Session
        fields = ['date', 'time', ]
        widgets = {
            'date': DatePickerInput(),
            'time': TimePickerInput(),
        }


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms
                               .TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms
                             .TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileForm(forms.ModelForm):
    name = forms.TextInput()
    photo = forms.ImageField()
    bio = forms.TextInput()

    class Meta:
        model = VolunteerProfile
        fields = ['name', 'photo', 'bio']
