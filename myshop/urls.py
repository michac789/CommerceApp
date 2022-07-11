from django.urls import path
from . import views

app_name = "myshop"
urlpatterns = [
    path("", views.main, name="main"),
    path("create", views.create, name="create"),
]
