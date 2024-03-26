from django.shortcuts import render, redirect
from .forms import SignUpForm


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signup success")
        else:
            form = SignUpForm()
        return render(request, "signup.html", {"form": form})


def signup_success(request):
    return render(request, "signup_success.html")


# Create your views here.
