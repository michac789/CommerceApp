from django.urls import path
# from django.conf.urls.static import static
# from django.conf import settings
from . import views

app_name = "catalog"
urlpatterns = [
    path("", views.main, name="main"),
    path("catalog", views.index, name="index"),
    path("catalog/<int:item_id>", views.item, name="item"),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
