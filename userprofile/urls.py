from django.urls import path
from .views import ProfileView, AllChat, ViewChat, FetchChat, PurchaseHistory


app_name = "userprofile"
urlpatterns = [
    path("view/<str:username>", ProfileView.as_view(), name="profile"),
    path("chats", AllChat.as_view(), name="chats"),
    path("chats/<str:username>", ViewChat.as_view(), name="chat"),
    path("chats/api/<str:username>", FetchChat.as_view()),
    path("history", PurchaseHistory.as_view(), name="history"),
]
