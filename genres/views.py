from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView,  UpdateView

from .models import Genre
# Create your views here.

class GenreListView(ListView):
    model = Genre
    context_object_name = 'genres'

class GenreDetailView(DetailView):
    model = Genre
    context_object_name = 'genre'

class GenreCreateView(CreateView):
    model = Genre
    success_url = reverse_lazy('genre_list')

class GenreUpdateView(UpdateView):
    model = Genre
    success_url = reverse_lazy('genre_detail')

class GenreDeleteView(DeleteView):
    model = Genre
    success_url = reverse_lazy('genre_list')


