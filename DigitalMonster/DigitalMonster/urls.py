"""
    DigitalMonster URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView



urlpatterns = [
    path('', RedirectView.as_view(url='/monsters/')),
    path('admin/', admin.site.urls),
    path('monsters/', include("monsters.urls"))
]
