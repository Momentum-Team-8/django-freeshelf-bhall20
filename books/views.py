from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Categories
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.
def hompage(request):
    if request.user.is_authenticated:
        return("book_list")
    return render(request, "books/homepage.html")

@login_required
def book_list(request):
    books = Book.objects.all().order_by('created_date')
    return render(request, 'books/book_list.html', {'books': books})

def show_categories(request, slug):
    categories = get_object_or_404(Categories, slug=slug)
    books = categories.books.all()

    return render(request, "books/show_categories.html", {"categories": categories, "books":books})