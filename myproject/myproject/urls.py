from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include

urlpatterns = [
    path('', include('admin_soft.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]
