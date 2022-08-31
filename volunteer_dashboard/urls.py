from django.urls import path
from . import views
from .views import VolunteerList, profile

urlpatterns = [
    path('', VolunteerList.as_view(), name='dashboard'),
    path('add_sessions/', views.add_sessions, name='add_sessions'),
    path('profile/', profile, name='profile'),
    path('<int:pk>/delete_session/',
         views.DeleteSession.as_view(),
         name='delete_session'),
    path('<int:pk>/edit_session/',
         views.EditSession.as_view(),
         name='edit_session'),
]
