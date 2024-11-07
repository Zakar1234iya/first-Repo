from django.urls import path
from . import views    # the . indicates that the views file can be found in the same directory as this file
                    
urlpatterns = [
    path('', views.index),
    path('add_dojo',views.create_new_dojo),
    path('add_ninja',views.create_new_ninja),
    path('delete_dojo/<int:dojo_id>/', views.delete_dojo , name='delete_dojo'),
]

