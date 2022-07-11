from django.urls import path
from . import views

app_name = "catalog"
urlpatterns = [
    path("", views.main, name="main"),
    path("catalog", views.index, name="index"),
    path("catalog/<int:item_id>", views.item, name="item"),
]
