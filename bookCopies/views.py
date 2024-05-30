from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BookCopy
# Create your views here.

class BookCopyListView(ListView):
    model = BookCopy
    context_object_name = 'bookcopies'

class BookCopyDetailView(DetailView):
    model = BookCopy
    context_object_name = 'bookcopy'

class BookCopyCreateView(CreateView):
    model = BookCopy
    success_url = reverse_lazy('book_copies_list')

class BookCopyUpdateView(UpdateView):
    model = BookCopy
    success_url = reverse_lazy('book_copies_detail')

class BookCopyDeleteView(DeleteView):
    model = BookCopy
    success_url = reverse_lazy('book_copies_list')


