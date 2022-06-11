from django.contrib import admin
from .models import Session, VolunteerProfile



@admin.register(VolunteerProfile)
class BioAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'photo', 'email', 'bio')
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'status')
    search_fields = ['date']
