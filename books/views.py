from django.shortcuts import render
from .models import Book
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.
def hompage(request):
    if request.user.is_authenticated:
        return("books_list")
        return render(request, "books/hompage.html")

@login_required
def book_list(request):
    book = Book.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'books/book_list.html', {'book': book})