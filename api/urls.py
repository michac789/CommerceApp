from django.urls import path
from . import views

app_name = "api"
urlpatterns = [
    path("", views.test),
    path("bookmark/<int:item_id>", views.bookmark),
    path("cart/<int:item_id>", views.addcart),
    path("buy", views.Buy.as_view()),
]
