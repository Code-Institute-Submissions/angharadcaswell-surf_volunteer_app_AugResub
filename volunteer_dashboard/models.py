from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class VolunteerProfile(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    photo = CloudinaryField('image', null= True, default='placeholder')
    bio = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return str(self.name)

class Session(models.Model):
    date = models.DateField()
    time = models.TimeField()
    status = models.BooleanField(default=False)
    volunteers = models.ManyToManyField('VolunteerProfile')

    
    def __str__(self):
        return str(self.date)

    def number_of_volunteers(self):
        return self.volunteers.count()
