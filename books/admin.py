from django.contrib import admin
from .models import User, Book, Categories
from books.models import User
from django.contrib import admin
# Register your models here.

admin.site.register(User)
admin.site.register(Book)
admin.site.register(Categories)