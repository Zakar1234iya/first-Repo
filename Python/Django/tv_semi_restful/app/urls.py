from django.urls import path
from . import views    

urlpatterns = [
    path('', views.index),
    path('shows', views.show_all, name='show_all'), #Displays all the shows. GET
    path('shows/new', views.add_new, name='add_new'), # Displays a form for adding a new TV show. GET
    path('shows/create', views.create_new, name='create_new'),# add new TV show and redirect for that page. POST
    path('shows/<int:id>', views.view_show, name='view_show'),# Displays the details of a specific show.GET
    path('shows/<int:id>/edit', views.edit_show, name='edit_show'),#Displays a form for editing a specific show. GET
    path('shows/<int:id>/update', views.update_show, name='update_show'),#the form submission to update a specific show.POST
    path('shows/<int:id>/destroy', views.delete_show, name='delete_show'), #delete a specific show. POST
 
]
