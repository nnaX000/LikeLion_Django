# urls.py

from django.urls import path
from . import views

# urls.py
urlpatterns = [
    path("logout/", views.logout, name="logout"),
    path("signup/", views.register, name="signup"),
    path("login-form/", views.login, name="loginForm"),  # 여기를 수정했습니다.
    path("signup/success/", views.signup_success, name="signup_success"),
    path("", views.root_redirect),  # 루트 URL에 대한 패턴
    path("login/", views.login_view, name="login"),  # 로그인 URL 패턴
]
