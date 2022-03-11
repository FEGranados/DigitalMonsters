"""
    DigitalMonster URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('monsters/', include("monsters.urls"))
]
