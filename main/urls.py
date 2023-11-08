from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path("", mainpage, name="mainpage"),
    path("choose/", choose, name="choose"),
    path("create/", create, name="create"),
    path("<int:funding_id>/", detail, name="detail"),
    path("payhistory/", payhistory, name="payhistory"),
    # path("edit/<int:fundings_id>/", update, name="edit"),
    path("present/", present, name="present"),
    path("soso/", soso, name="soso"),
    path("dream/", dream, name="dream"),
    path("delete/<int:funding_id>/", delete, name="delete"),
    path("update/<int:funding_id>/", update, name="update"),
    # path("like/<int:funding_id>/", like, name="like"),
    path("funding_like_toggle", funding_like_toggle, name="funding_like_toggle"),
]
