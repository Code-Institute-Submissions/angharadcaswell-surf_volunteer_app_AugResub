from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class VolunteerProfile(models.Model):
    user = models.OneToOneField(User, null= True, related_name='profile', on_delete=models.CASCADE)
    photo = CloudinaryField('image', default='placeholder')
    bio = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.user.username

class Session(models.Model):
    date = models.DateField()
    time = models.TimeField()
    status = models.BooleanField(default=False)
    volunteers = models.ManyToManyField('VolunteerProfile')

    
    def __str__(self):
        return str(self.date)

    def number_of_volunteers(self):
        return self.volunteers.count()
