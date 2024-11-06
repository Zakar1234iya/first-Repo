from django.urls import path
from . import views

urlpatterns = [
    path('/register', views.register),
    path('/login', views.login),
    path('/user/new', views.root),
    path('/user', views.user),
    path("/" ,views.my_view),
]
