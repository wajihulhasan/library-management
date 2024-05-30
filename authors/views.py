from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from authors.models import Author


# Create your views here.
class AuthorListView(ListView):
    model = Author
    context_object_name = 'authors'

class AuthorDetailView(DetailView):
    model = Author
    context_object_name = 'author'

class AuthorCreateView(CreateView):
    model = Author
    success_url = reverse_lazy('author_list')

class AuthorUpdateView(UpdateView):
    model = Author
    success_url = reverse_lazy('author_detail')


class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('author_list')

