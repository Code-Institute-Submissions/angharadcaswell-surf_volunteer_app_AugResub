from django.urls import path
from . import views


urlpatterns = [
    path('editprofile/', views.EditProfile.as_view(), name='edit_profile'),
]

