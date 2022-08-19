from django.urls import path
from .views import ViewCart, Buy

app_name = "cart"
urlpatterns = [
    path("", ViewCart.as_view(), name="main"),
    path("buy", Buy.as_view(), name="buy"),
]
