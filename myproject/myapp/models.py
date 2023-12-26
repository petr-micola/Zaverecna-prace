from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False, default=None)
    username = models.CharField(max_length=30, unique=True, blank=False, null=False)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='img/Sample_User_Icon.png', blank=True, null=True)
