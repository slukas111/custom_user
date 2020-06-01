from django.urls import path
from sashauser import views

urlpatterns = [
    path("", views.index, name="home"),
    path("register/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
