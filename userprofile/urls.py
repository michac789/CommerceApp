from django.urls import path
from . import views

app_name = "userprofile"
urlpatterns = [
    path("view/<str:username>", views.profile, name="profile"),
    path("chats", views.chats, name="chats"),
    path("chats/<int:chat_id>", views.chatcontent, name="chatcontent"),
]
