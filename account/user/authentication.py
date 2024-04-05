# your_project/your_app/authentication.py

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

User = get_user_model()


class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, user_id=None, password=None):
        try:
            user = User.objects.get(user_id=user_id)
            if user and check_password(password, user.password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
