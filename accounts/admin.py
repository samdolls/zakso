from django.contrib import admin
from .models import CustomUser, CustomUserManager

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'username',
        'password',
        'birth_date',
        'phone_number',
        'is_active',
    )
