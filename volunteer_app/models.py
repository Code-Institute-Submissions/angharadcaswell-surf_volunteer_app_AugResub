from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Session(models.Model):
    date = models.DateField()
    time = models.TimeField()
    volunteers = models.ForeignKey('VolunteerProfile', null=True, on_delete=models.SET_NULL)
    full = models.BooleanField(default=False)

    def __str__(self):
        return self.date

    def number_of_volunteers(self):
        return self.volunteers.count()

class VolunteerProfile(models.Model):
    name = models.CharField(max_length=80, unique=True)
    photo = CloudinaryField('image', null= True, default='placeholder')
    bio = models.TextField()
    email = models.EmailField()
    sessions = models.ForeignKey('Session', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)