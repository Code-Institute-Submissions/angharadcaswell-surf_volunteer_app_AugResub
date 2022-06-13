from volunteer_app.models import Session, VolunteerProfile
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
        fields = ('date', 'time',)
        widgets = {
            'date' : DatePickerInput(),
            'time' : TimePickerInput(),
        }

# class ProfileForm(forms.ModelForm):

#     class Meta:
#         model = VolunteerProfile
#         fields = ('name', 'email', 'photo', 'bio')

        