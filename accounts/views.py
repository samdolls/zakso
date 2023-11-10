from django.shortcuts import render, redirect
from .models import CustomUser, UserProfile
from .forms import UserForm
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_protect
from django.contrib.sessions.models import Session
from main.models import Fundings
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


@csrf_protect

# 회원가입
def signup(request):
    if request.method == "POST":
        agree = request.POST.get("agree")
        if agree == "on":
            form = UserForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect("accounts:login_view")
            else:
                errors = form.errors
                print(errors)
        else:
            return render(request, "signup.html", {"error": "약관에 동의해주세요."})
    else:
        form = UserForm()
    return render(request, "signup.html", {"form": form})


# 로그인
def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        remember_me = request.POST.get("remember_me")
        stay_login = request.POST.get("stay_login")

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)

            if not remember_me:
                request.session.set_expiry(0)  # 세션 유지 시간을 0으로(브라우저 끝나면 끝)
            elif stay_login:
                request.session.set_expiry(1209600)  # 세션 유지 시간을 2주로(자동 로그인한다면)

            return redirect("main:mainpage")
        else:
            return render(
                request, "login_false.html", {"error": "이메일 또는 비밀번호가 올바르지 않습니다."}
            )
    else:
        return render(request, "login.html")


# 로그아웃
def logout_view(request):
    logout(request)
    return redirect("main:mainpage")


def home(request):
    return render(request, "home.html")


@login_required
def mypage_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    user_post = Fundings.objects.filter(writer=request.user)
    user_like_post = Fundings.objects.filter(like=request.user)
    return render(request, 'mypage.html', {'user_profile':user_profile, 'user_post':user_post, 'user_like_post':user_like_post})

@require_POST
@login_required
def funding_like_toggle(request):
    pk = request.POST.get('pk', None)
    funding = Funding.objects.get(pk=pk)
    user = request.user

    if funding.like.filter(id=user.id).exists():
        funding.like.remove(user)
        result = 'unlike'
    else:
        funding.like.add(user)
        result = 'like'

    likes_cnt = funding.like.count()
    
    return JsonResponse({'result': result, 'likes_cnt': likes_cnt})
    
@login_required
def menu_log(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, "menu_log.html", {"user_profile": user_profile})


def menu_out(request):
    return render(request, "menu_out.html") 

def qrcode(request):
    return render(request, 'qrcode.html')