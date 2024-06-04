from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    UpdateView,
)

from .forms import GenreForm
from .models import Genre

# Create your views here.


class GenreListView(ListView):
    model = Genre
    context_object_name = "genres"
    template_name = "genres/genres_list.html"


class GenreDetailView(DetailView):
    model = Genre
    context_object_name = "genre"
    template_name = "genres/genre_detail.html"


class GenreCreateView(CreateView):
    model = Genre
    form_class = GenreForm
    success_url = reverse_lazy("genres:genre_list")


class GenreUpdateView(UpdateView):
    model = Genre
    form_class = GenreForm

    def get_success_url(self):
        return reverse("genres:genre_detail", kwargs={"pk": self.object.pk})


class GenreDeleteView(DeleteView):
    model = Genre
    success_url = reverse_lazy("genre_list")
