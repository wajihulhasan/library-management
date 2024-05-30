from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView,  UpdateView

from books.models import Book


# Create your views here.


class BookListView(ListView):
    model = Book
    context_object_name = 'books'

class BookCreateView(CreateView):
    model = Book
    fields = "__all__"
    success_url = reverse_lazy('book_list')


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')


class BookUpdateView(UpdateView):
    model = Book
    fields = "__all__"
    success_url = reverse_lazy('book_list')
