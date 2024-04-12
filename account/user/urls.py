from django.contrib.auth.views import LoginView
from django.urls import path
from user.views import signup
from user import views as user_views  # myapp의 views를 임포트합니다.
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("profile/", user_views.profile_view, name="profile"),
    path("login/", user_views.custom_login_view, name="login"),
    path("home/", user_views.home, name="home"),
    path("logout/", user_views.my_logout_view, name="logout"),
    path("profile_redirect/", user_views.profile_redirect, name="profile_redirect"),
    path("my_profile/", user_views.my_profile, name="my_profile"),
    path("my_page/", user_views.my_page, name="my_page"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 추가: 개발 중에 미디어 파일 제공
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
