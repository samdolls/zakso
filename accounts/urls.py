from django.contrib import admin
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('signup/', views.signup, name='signup'),
    path('home/',views.home, name='home'),
    path('mypage/',views.mypage_view, name='mypage_view'),
    path('menu_log/', views.menu_log, name='menu_log'),
    path('menu_out/', views.menu_out, name='menu_out'),
    path('qrcode/', views.qrcode, name='qrcode'),
]
