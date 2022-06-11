from django.urls import path
from . import views


urlpatterns = [
    path('profile/', views.VolunteerPortfolio.as_view(), name='profile'),
    path('editprofile/', views.EditProfile.as_view(), name='edit_profile'),
]

