from django.urls import path
from . import views    

urlpatterns = [
    path('', views.view_books, name='view_books'),
    path('authors', views.view_authors, name='view_authors'),
    path('view_author/<int:id>', views.view_author, name='view_author'),
    path('library/<int:id>', views.view_book, name='view_book'),
    path('add_book', views.add_book, name='add_book'),
    path('add_author', views.add_author, name='add_author'),
    path('assign_book', views.assign_book, name='assign_book'),
    path('assign_author', views.assign_author, name='assign_author'),
]
