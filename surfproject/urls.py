from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('profile/', include('volunteer_app.urls'), name='profile'),
    path('editprofile/', include('volunteer_app.urls'), name='edit_profile'),
]
