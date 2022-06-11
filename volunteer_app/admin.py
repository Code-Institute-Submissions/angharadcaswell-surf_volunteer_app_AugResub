from django.contrib import admin
from .models import Session, VolunteerProfile



@admin.register(VolunteerProfile)
class PostAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('name',)}


# Register your models here.
admin.site.register(Session)
