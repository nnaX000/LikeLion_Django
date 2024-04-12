from django.shortcuts import render, redirect
from .forms import SignUpForm
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import CustomUser  # 커스텀 사용자 모델
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.core.files.storage import FileSystemStorage
from django.urls import reverse


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


@login_required
def my_profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form_data = request.POST
        image_file = request.FILES.get("image")

        if image_file:
            fs = FileSystemStorage()
            filename = fs.save(image_file.name, image_file)
            profile.image = filename  # 파일 경로를 저장
            # profile.image.save(filename, image_file, save=True) # 이 방식도 사용할 수 있음

            profile.keyword = form_data.get("keyword", profile.keyword)
            profile.mbti = form_data.get("mbti", profile.mbti)
            profile.hobbies = form_data.get("hobbies", profile.hobbies)
            profile.save()

            messages.success(request, "프로필 정보가 성공적으로 저장되었습니다!")
            return redirect(reverse("home"))  # 홈으로 리디렉션

    # GET 요청 시 사용자 정보를 폼에 미리 채워서 전달
    return render(request, "my_profile.html", {"profile": profile})


@login_required
def profile_redirect(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if not created and (
        profile.keyword or profile.mbti or profile.hobbies
    ):  # 정보가 이미 있는 경우
        return redirect(
            "my_profile"
        )  # 'my_profile'은 프로필을 보여주는 페이지의 URL name
    else:
        return redirect("my_page")  # 'my_page'는 프로필을 설정하는 페이지의 URL name


@login_required
def my_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    return render(request, "my_profile.html", {"profile": profile})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .models import UserProfile  # Make sure to import your UserProfile model correctly


@login_required
def my_page(request):
    profile = UserProfile.objects.get_or_create(user=request.user)[0]

    if request.method == "POST":
        form_data = request.POST
        image_file = request.FILES.get("image")

        if image_file:
            fs = FileSystemStorage()
            filename = fs.save(image_file.name, image_file)
            profile.image = (
                filename  # Save relative path to the image in the UserProfile
            )

        # Update text fields
        profile.keyword = form_data.get(
            "keyword", profile.keyword
        )  # Use existing value if field is empty
        profile.mbti = form_data.get("mbti", profile.mbti)
        profile.hobbies = form_data.get("hobbies", profile.hobbies)
        profile.save()

        return redirect("my_profile")  # Redirect to the 'my_profile' page after POST

    # Load initial form data from the existing profile
    initial_data = {
        "keyword": profile.keyword,
        "mbti": profile.mbti,
        "hobbies": profile.hobbies,
        "image_url": profile.image.url if profile.image else None,
    }

    return render(
        request, "my_page.html", initial_data
    )  # Pass initial data to the form in GET request
