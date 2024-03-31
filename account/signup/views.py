from django.shortcuts import render, redirect
from .forms import SignUpForm

# views.py

from django.shortcuts import redirect

# views.py에서 로그인 페이지를 렌더링하는 뷰를 추가합니다.


def login_view(request):
    # 로그인 처리 로직이 여기에 옵니다. (예시로만 제공됩니다)
    return render(request, "login.html")  # 'login.html'은 로그인 페이지의 템플릿입니다.


def root_redirect(request):
    return redirect("login")  # 'login'은 로그인 페이지의 URL 이름입니다.


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signup_success")  # 경로 이름을 확인하세요
    else:
        form = SignUpForm()  # 이 부분을 if 블록 바깥으로 이동
    return render(
        request, "signup.html", {"form": form}
    )  # 들여쓰기를 조정하여 항상 실행되게 함


def signup_success(request):
    return render(request, "signup_success.html")


# Create your views here.
