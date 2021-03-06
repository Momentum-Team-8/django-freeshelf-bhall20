from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path("books/", views.book_list, name="book_list"),
    path("categories/<slug:slug>", views.show_categories, name="show_categories"),
]