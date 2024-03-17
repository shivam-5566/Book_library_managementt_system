

# Create your views here.
from django.shortcuts import render, redirect
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        description = request.POST['description']
        Book.objects.create(title=title, author=author, description=description)
        return redirect('book_list')
    return render(request, 'add_book.html')
