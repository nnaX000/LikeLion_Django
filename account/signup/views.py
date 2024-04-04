from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm

# views.py

from django.shortcuts import redirect

# views.py에서 로그인 페이지를 렌더링하는 뷰를 추가합니다.


def home(request):
    # 로그인 처리 로직이 여기에 옵니다. (예시로만 제공됩니다)
    return render(request, "home.html")  # 'l


def logout(request):
    # 로그인 처리 로직이 여기에 옵니다. (예시로만 제공됩니다)
    return render(
        request, "logout.html"
    )  # 'login.html'은 로그인 페이지의 템플릿입니다.


def login_view(request):
    # 로그인 처리 로직이 여기에 옵니다. (예시로만 제공됩니다)
    return render(request, "login.html")  # 'login.html'은 로그인 페이지의 템플릿입니다.


def login(request):
    # 로그인 처리 로직이 여기에 옵니다. (예시로만 제공됩니다)
    return render(
        request, "loginForm.html"
    )  # 'login.html'은 로그인 페이지의 템플릿입니다.


def root_redirect(request):
    return redirect("home")  # 'login'은 로그인 페이지의 URL 이름입니다.


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signup_success")  # 경로 이름을 확인하세요
    else:
        form = CustomUserCreationForm()  # 이 부분을 if 블록 바깥으로 이동
    return render(
        request, "signup.html", {"form": form}
    )  # 들여쓰기를 조정하여 항상 실행되게 함


def signup_success(request):
    return render(request, "signup_success.html")


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # 데이터베이스에 저장하지 않고 인스턴스 생성
            user.set_password(form.cleaned_data["password"])  # 비밀번호 해시 설정
            user.save()  # 변경사항을 포함하여 모델 인스턴스를 데이터베이스에 저장
            login(request, user)  # 사용자 로그인
            return redirect("home")  # 등록 후 리디렉션
    else:
        form = CustomUserCreationForm()
    return render(request, "signup.html", {"form": form})


# Create your views here.
