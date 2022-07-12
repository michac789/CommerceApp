from django.urls import path
from . import views

app_name = "myshop"
urlpatterns = [
    path("", views.main, name="main"),
    path("create", views.create, name="create"),
    path("edit/<int:item_id>", views.edit, name="edit"),
    path("register", views.register, name="register"),
]
