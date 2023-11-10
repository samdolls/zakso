from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path("", mainpage, name="mainpage"),
    path("choose/", choose, name="choose"),
    path("before_create/", before_create, name="before_create"),
    path("create/", create, name="create"),
    path("<int:funding_id>/", detail, name="detail"),
    path("finish/<int:funding_id>/", finish, name="finish"),
    path("payhistory/", payhistory, name="payhistory"),
    path("before_update/<int:funding_id>/", before_update, name="before_update"),
    path("update/<int:funding_id>/", update, name="update"),
    path("present/", present, name="present"),
    path("soso/", soso, name="soso"),
    path("dream/", dream, name="dream"),
    path("delete/<int:funding_id>/", delete, name="delete"),
    path("after_create/<int:funding_id>/", after_create, name="after_create"),
    # path("like/<int:funding_id>/", like, name="like"),
    path("funding_like_toggle", funding_like_toggle, name="funding_like_toggle"),
    path("search/", search, name="search"),
]
