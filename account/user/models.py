from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.conf import settings


class CustomUser(AbstractUser):
    major = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    user_id = models.CharField(max_length=50, unique=True)  # 사용자 정의 ID 필드


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    image = models.ImageField(upload_to="profiles/", default="profiles/default.jpg")
    keyword = models.CharField(max_length=100, blank=True)
    mbti = models.CharField(max_length=4, blank=True)
    hobbies = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
