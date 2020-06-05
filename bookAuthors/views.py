from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request): 
    context = {
        "books" : book.objects.all(),
        "authors" : author.objects.all()
    }
    return render(request, "index.html", context)

def addBook(request):
    book.objects.create(title=request.POST['title'],desc=request.POST['desc'])
    return redirect('/')

def books(request, bookid):
    # Create list of authors excluding the authors of requested book
    availableAuthors = []
    for a_author in author.objects.all():
        if a_author not in book.objects.get(id=bookid).authors.all():
            availableAuthors.append(a_author)
    
    context = {
        "book" : book.objects.get(id=bookid),
        "authors" : availableAuthors
    }
    return render(request, "book.html", context)

def addAuthor(request, bookid):
    # Add the selected author as an author to the current book displayed
    book.objects.get(id=bookid).authors.add(author.objects.get(id=request.POST['selectedAuthor']))
    
    return redirect(f'/books/{bookid}/')

def addAuthors(request):
    context = {
        "authors" : author.objects.all()
    }
    return render(request, "authors.html", context)

def createAuthor(request):
    author.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'],notes=request.POST['notes'])
    return redirect("/authors/")

def getAuthor(request, authorid):
    availableBooks = []
    for a_book in book.objects.all():
        if a_book not in author.objects.get(id=authorid).books.all():
            availableBooks.append(a_book)
    
    context = {
        "books" : availableBooks,
        "author" : author.objects.get(id=authorid)
    }
    return render(request, "author.html", context)

def addBookToAuthor(request, authorid):
    # Add the selected book to the currently displayed author's books
    author.objects.get(id=authorid).books.add(book.objects.get(id=request.POST['selectedBook']))

    return redirect(f'/authors/{authorid}/')