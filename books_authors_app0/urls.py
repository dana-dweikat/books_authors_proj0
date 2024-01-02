from django.urls import path

from . import views

app_name = 'books_authors_app0'  # Add this line to specify the app name

urlpatterns = [
    path('', views.books, name='books'),
    path('books/<int:pk>',views.book_details, name='details'),
    path('books/add/<int:pk>',views.add_author_to_book, name='add_book'),
    path('authors', views.authors, name='authors'),
    path('author_details/<int:pk>',views.author_details, name='author_details'),
    path('author/add/<int:pk>',views.add_book_to_author, name='add_author')

]