from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('submit' , views.create_new_user)
]
