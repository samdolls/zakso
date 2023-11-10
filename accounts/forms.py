from django import forms
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    phone_number = forms.CharField(max_length=15, label="전화번호")
    birth_date = forms.CharField(max_length=6, label="생년월일")

    class Meta:
        model = CustomUser
        fields = ["email", "username", "phone_number", "birth_date"]

    def clean_birth_date(self):
        birth_date = self.cleaned_data.get("birth_date")

        if birth_date and len(birth_date) == 6:
            current_year = datetime.now().year  # 현재 년도를 가져옴
            year = birth_date[:2]
            if int(year) >= current_year % 100:  # 현재 년도의 뒷 두 자리와 비교
                year = "19" + year
            else:
                year = "20" + year

            month = birth_date[2:4]
            day = birth_date[4:]
            formatted_date = f"{year}-{month}-{day}"
            try:
                birth_date_obj = datetime.strptime(formatted_date, "%Y-%m-%d").date()
                return birth_date_obj
            except ValueError:
                raise forms.ValidationError("올바른 형식의 생년월일을 입력하세요.")

        raise forms.ValidationError("올바른 형식의 생년월일을 입력하세요.")
