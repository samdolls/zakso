from django.urls import path
from .views import *

app_name = "payments"
urlpatterns = [
    path("", index, name="index"),
    path("success", success, name="success"),
    path("fail", fail, name="fail"),
]
