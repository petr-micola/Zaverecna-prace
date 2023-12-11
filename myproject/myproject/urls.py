from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include

from myapp.views import home

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]
