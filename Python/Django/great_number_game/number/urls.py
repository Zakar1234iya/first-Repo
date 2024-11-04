from django.urls import *     
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('guess', views.guess, name='guess'),
    path('restart', views.restart, name='restart'),
    path('highscore', views.highscore, name='highscore'),
    path('save_score', views.save_score, name='save_score'),
    ]
