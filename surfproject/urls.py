from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'), name='home'),
    path('dashboard/', include('volunteer_dashboard.urls')),
    path('accounts/', include('allauth.urls')),
]
