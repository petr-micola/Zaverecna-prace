from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from myapp.views import *

urlpatterns = [
    path('', quiz, name='quiz'),
    path('accounts/', include('allauth.urls')),
    path('account/view', view_account, name='view_account'),
    path('account/edit', edit_account, name='edit_account'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
