from django.contrib.auth.views import LoginView
from django.urls import path
from user.views import signup
from user import views as user_views  # myapp의 views를 임포트합니다.

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("profile/", user_views.profile_view, name="profile"),
    path("login/", user_views.custom_login_view, name="login"),
    path("home/", user_views.home, name="logout"),
]
