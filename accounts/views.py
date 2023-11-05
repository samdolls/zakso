from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import UserForm
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_protect
from django.contrib.sessions.models import Session
@csrf_protect

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
    return render(request, 'signup.html', {'form':form})

# 로그인
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        remember_me = request.POST.get('remember_me')
        stay_login = request.POST.get('stay_login')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)

            if not remember_me:
                request.session.set_expiry(0)  # 세션 유지 시간을 0으로(브라우저 끝나면 끝)
            elif stay_login:
                request.session.set_expiry(1209600)  # 세션 유지 시간을 2주로(자동 로그인한다면)

            return redirect('accounts:home')
        else:
            return render(request, 'login.html', {'error': '이메일 또는 비밀번호가 올바르지 않습니다.'})
    else:
        return render(request, 'login.html')

# 로그아웃
def logout_view(request):
    logout(request)
    return redirect('accounts:login_view')

def home(request):
    return render(request, 'home.html')

