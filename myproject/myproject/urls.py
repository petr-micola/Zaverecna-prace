from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include

from myapp.views import *

urlpatterns = [
    path('', view_profile, name='view_profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]
