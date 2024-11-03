from django.urls import *     
from . import views

urlpatterns = [
    path('', views.index),       
    path('result', views.survey_result),   
    ]