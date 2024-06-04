from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView

from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)

from .forms import BookCopiesForm
from .models import BookCopy

# Create your views here.


class BookCopyListView(ListView):
    model = BookCopy
    context_object_name = "bookcopies"
    template_name = "bookCopies/book_copy_list.html"


class BookCopyDetailView(DetailView):
    model = BookCopy
    template_name = "bookCopies/book_copy_detail.html"
    context_object_name = "bookcopy"


class BookCopyCreateView(CreateView):
    model = BookCopy
    form_class = BookCopiesForm
    template_name = "bookCopies/book_copy_form.html"
    success_url = reverse_lazy("bookCopies:book_copies_list")


class BookCopyUpdateView(UpdateView):
    model = BookCopy
    form_class = BookCopiesForm
    template_name = "bookCopies/book_copy_form.html"

    def get_success_url(self):
        return reverse("bookCopies:book_copies_detail", kwargs={"pk": self.object.pk})


class BookCopyDeleteView(DeleteView):
    model = BookCopy
    template_name = "bookCopies/book_copy_confirm_delete.html"
    success_url = reverse_lazy("bookCopies:book_copies_list")
