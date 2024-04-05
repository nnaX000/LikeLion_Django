from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    major = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    user_id = models.CharField(max_length=50, unique=True)  # 사용자 정의 ID 필드
