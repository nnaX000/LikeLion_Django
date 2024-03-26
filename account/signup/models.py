from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    id = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    major = models.CharField(max_length=20)
    nickname = models.CharField(max_length=10)
    password = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=13)


# Create your models here.
