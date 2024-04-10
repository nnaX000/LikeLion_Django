from django.shortcuts import render, redirect
from .forms import SignUpForm
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import CustomUser  # 커스텀 사용자 모델
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile


def home(request):
    return render(request, "home.html")


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")  # 'login'은 로그인 페이지의 URL 이름입니다.
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})


def profile_view(request):
    return render(request, "profile.html", {"user": request.user})


def custom_login_view(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        password = request.POST.get("password")
        user = authenticate(
            request, user_id=user_id, password=password
        )  # 사용자 인증 시도
        if user is not None:
            login(request, user)  # 세션에 사용자 정보 추가
            return redirect("profile")  # 프로필 페이지로 리디렉션
        else:
            messages.error(
                request, "일치하는 회원정보가 없습니다. 다시 시도해주세요."
            )  # 오류 메시지
    return render(request, "login.html")  # 로그인 페이지 렌더링


def my_logout_view(request):
    logout(request)
    return redirect("home")  # 홈으로 리다이렉트


def my_page(request):
    return render(request, my_page.html)


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile


@login_required
def my_profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        profile.image = request.FILES.get("image", profile.image)
        profile.keyword = request.POST.get("keyword", "")
        profile.mbti = request.POST.get("mbti", "")
        profile.hobbies = request.POST.get("hobbies", "")
        profile.save()
        return redirect("home")  # Redirect to the home page

    return render(request, "my_page.html", {"profile": profile})
