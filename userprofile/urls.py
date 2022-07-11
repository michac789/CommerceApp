from django.urls import path
from . import views

app_name = "userprofile"
urlpatterns = [
    path("<str:username>", views.profile, name="profile"),
]
