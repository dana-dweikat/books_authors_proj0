from django.shortcuts import render, redirect, get_object_or_404

from .models import Book, Author
from .forms import BookForm , AuthorForm


def books(request):
    books = Book.objects.all()
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('books_authors_app0:books')

    context = {
        'books': books,
         'form': form
    }
    return render(request, 'books.html', context)


def book_details(request, pk):
    
    #book = Book.objects.get(id=pk)
    book = get_object_or_404(Book, id=pk)
    book_authors = book.authors.all()
    authors = Author.objects.all()

    context = {'book': book, 'book_authors': book_authors, 'authors': authors}
    return render(request, "book_details.html", context)


def add_author_to_book(request, pk):
    book = Book.objects.get(id=pk)
    author_id = request.POST['bbb']
    author = Author.objects.get(id=author_id)
    book.authors.add(author)
    book.save()

    return redirect('books_authors_app0:details', pk=pk)




def authors(request):
    author = Author.objects.all()
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('books_authors_app0:authors')
    
    context = {
        'author': author,
        'form': form
    }

    return render(request, 'authors.html', context)


def author_details(request, pk):

    author = Author.objects.get(id=pk)
    books_authors = author.book_set.all()
    books = Book.objects.all()

    context = {
        'books_of_author': books_authors,
        'author': author,
        'books': books
        }
    
    return render(request, "author_details.html", context)


def add_book_to_author(request, pk):
    author = Author.objects.get(id=pk)
    book_id = request.POST['bbb']
    book = Book.objects.get(id=book_id)
    book.authors.add(author)
    book.save()
    
    return redirect('books_authors_app0:author_details', pk=pk)