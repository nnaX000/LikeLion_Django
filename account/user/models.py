from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone


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


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts"
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to="posts/%Y/%m/%d/", blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # 객체가 생성될 때의 시각을 자동 저장
    updated_at = models.DateTimeField(
        auto_now=True
    )  # 객체가 저장될 때의 시각을 자동 업데이트

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="likes"
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("user", "post"),)  # Ensure a user can like a post only once

    def __str__(self):
        return f"{self.user.username} likes {self.post.title}"


class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments"
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"
