# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("signup/success/", views.signup_success, name="signup_success"),
    # 기타 URL 패턴...
]
