from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addBook/', views.addBook),
    path('books/<int:bookid>/', views.books),
    path('books/<int:bookid>/addAuthor/', views.addAuthor),
    path('authors/', views.addAuthors),
    path('authors/createAuthor/', views.createAuthor),
    path('authors/<int:authorid>/', views.getAuthor),
    path('authors/<int:authorid>/addBook/', views.addBookToAuthor)
]