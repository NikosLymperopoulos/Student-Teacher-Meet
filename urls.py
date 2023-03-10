from register import views
from . import views
from django.urls import path

urlpatterns = [
    path("loggedin/", views.loggedin, name="loggedin"),
    path("login_user/", views.login_user, name="login_user"),
    path("logout_user/", views.logout_user, name="logout_user"),
]
