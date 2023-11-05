from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserForm(UserCreationForm):
    email = forms.EmailField(label='이메일')
    phone_number = forms.CharField(max_length=15, label='전화번호')
    birth_date = forms.DateField(label='생년월일')

    class Meta:
        model = CustomUser
        fields = ['email','username','phone_number','birth_date']