from django.urls import path     
from . import views


urlpatterns = [
    path('', views.index),
    path('/register' , view.register),   
    path('login', view.login),
]