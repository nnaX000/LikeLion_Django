from django.shortcuts import render, redirect
from .forms import SignUpForm


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
