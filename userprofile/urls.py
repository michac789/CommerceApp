from django.urls import path
from .views import ProfileView, ViewChat, FetchChat
from . import views

app_name = "userprofile"
urlpatterns = [
    path("view/<str:username>", ProfileView.as_view(), name="profile"),
    path("chats", views.chats, name="chats"),
    path("chats/<int:chat_id>", views.chatcontent, name="chatcontent"),

    path("chats/<str:username>", ViewChat.as_view()),
    path("chats/api/<str:username>", FetchChat.as_view()),
]
