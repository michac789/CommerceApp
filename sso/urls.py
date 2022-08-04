from django.urls import path
from . import views

app_name = "sso"
urlpatterns = [
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
    path("t&c", views.tc, name="tc"),
    
    # WARNING!!! This route below is only used once to load mock data!
    # Once it is loaded, do not call it again, unless you want to empty the
    # whole database first!
    # path("loadseeds", views.seed),
]
