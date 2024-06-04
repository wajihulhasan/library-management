from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView

from django.views.generic.edit import (
    CreateView,
    DeleteView,
    UpdateView,
)

from books.forms import BookForm
from books.models import Book


# Create your views here.


class BookListView(ListView):
    model = Book
    context_object_name = "books"
    template_name = "books/books_list.html"


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy("books:book_list")


class BookDetailView(DetailView):
    model = Book
    context_object_name = "book"


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy("books:book_list")


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm

    def get_success_url(self):
        return reverse("books:book_detail", kwargs={"pk": self.object.pk})
