from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import UserForm
from django.contrib.auth import login, authenticate, logout


#회원가입
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:login_view')
        else:
            errors = form.errors
            print(errors)
    else:
        form = UserForm()
    return render(request, "signup.html", {"form": form})


# 로그인
def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("main:mainpage")
        else:
            return render(request, "login.html", {"error": "이메일 또는 비밀번호가 올바르지 않습니다."})
    else:
        return render(request, "login.html")


# 로그아웃
def logout_view(request):
    logout(request)
    return redirect("main:mainpage")


def home(request):
    return render(request, "home.html")
