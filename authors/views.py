from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from authors.forms import AuthorForm
from authors.models import Author


# Create your views here.
class AuthorListView(ListView):
    model = Author
    context_object_name = "authors"
    template_name = "authors/authors_list.html"


class AuthorDetailView(DetailView):
    model = Author
    context_object_name = "author"
    template_name = "authors/author_detail.html"


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy("authors:author_list")


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    pk_url_kwarg = "pk"

    def get_success_url(self):
        return reverse("authors:author_detail", kwargs={"pk": self.object.pk})


class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy("authors:author_list")
