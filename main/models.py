from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import CustomUser

# Create your models here.


class Fundings(models.Model):
    TYPE_CHOICES = (
        ("선물 펀딩", _("선물 펀딩")),
        ("소소 펀딩", _("소소 펀딩")),
        ("드림 펀딩", _("드림 펀딩")),
    )
    BANK_CHOICES = (
        ("저축은행", _("저축은행")),
        ("농협은행", _("농협은행")),
        ("우리은행", _("우리은행")),
        ("기업은행", _("기업은행")),
        ("국민은행", _("국민은행")),
        ("신한은행", _("신한은행")),
        ("하나은행", _("하나은행")),
        ("외환은행", _("외환은행")),
        ("씨티은행", _("씨티은행")),
        ("부산은행", _("부산은행")),
        ("대구은행", _("대구은행")),
        ("전북은행", _("전북은행")),
        ("경남은행", _("경남은행")),
        ("제주은행", _("제주은행")),
        ("우체국", _("우체국")),
        ("새마을금고", _("새마을금고")),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default="선물 펀딩")
    title = models.CharField(max_length=50)
    writer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.CharField(max_length=50)
    total_price = models.IntegerField()
    accumulation = models.IntegerField(default=0)
    percentage = models.IntegerField(default=0)
    content = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    funding_image = models.ImageField(upload_to="fundings/", blank=False, null=False)
    qr_image = models.ImageField(upload_to="qr/", blank=True, null=True)
    account_bank = models.CharField(
        max_length=50, default="", choices=BANK_CHOICES, blank=False, null=False
    )
    account_num = models.CharField(max_length=50, default="", blank=False, null=False)
    delievery = models.CharField(max_length=50, default="", blank=False, null=False)
    like = models.ManyToManyField(CustomUser, related_name="likes", blank=True)
    likes_cnt = models.IntegerField(default=0)
    is_private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


@receiver(post_save, sender=Fundings)
def update_percentage(sender, instance, **kwargs):
    try:
        total_price = int(instance.total_price)
        accumulation = int(instance.accumulation)
    except ValueError:
        total_price = 0
        accumulation = 0

    if total_price > 0:
        calculated_percentage = round((accumulation / total_price) * 100)
        print(calculated_percentage)
    else:
        calculated_percentage = 0

    if calculated_percentage != instance.percentage:
        instance.percentage = calculated_percentage
        instance.save()


class History(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    funding = models.ForeignKey(Fundings, on_delete=models.CASCADE)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
