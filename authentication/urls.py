from django.urls import path
from django.urls import include, path


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("signup", views.signup, name="signup"),
    path("shopping", include("shopping.urls"), name="shopping"),
    path("logout", views.logout_view, name="logout"),
    
]
