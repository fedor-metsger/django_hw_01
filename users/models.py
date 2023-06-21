
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = None

    email = models.EmailField(verbose_name='почта', unique=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    telegram = models.CharField(max_length=50, null=True, blank=True)
    avatar = models.ImageField(upload_to="users", null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []