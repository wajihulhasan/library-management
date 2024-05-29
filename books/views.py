from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView,  UpdateView

from books.models import Book


# Create your views here.


class BookListView(ListView):
    model = Book


class CreateBookView(CreateView):
    model = Book
    fields = "__all__"


class BookDetailView(DetailView):
    model = Book
class DeleteBookView(DeleteView):
    model = Book


class UpdateBookView(UpdateView):
    model = Book
    fields = "__all__"