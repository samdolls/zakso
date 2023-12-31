from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

    #커스텀키 생성
    @classmethod
    def create_key(cls):
        import random
        import string

        ket_length = 20
        characters = string.digits #숫자로 된 랜덤 문자열 생성
        return ''.join(random.choice(characters) for _ in range(ket_length))



class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=100)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    birth_date = models.DateField(null=True, blank=True)
    customer_key = models.CharField(max_length=100, unique=True, default=CustomUserManager().create_key)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email


    class Meta:
        app_label = 'accounts'
        db_table = 'custom_user'
        verbose_name = 'custom_user'
        verbose_name_plural = 'custom_user'

#mypage
class UserProfile(models.Model):
    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, default='')

    def save(self, *args, **kwargs):
        if not self.username:
            self.username=self.user.username
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


