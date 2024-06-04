from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import (
    CreateView,
    DeleteView,
    UpdateView, ListView, DetailView,
)

from .forms import PatronForm
from .models import Patron

# Create your views here.


class PatronListView(ListView):
    model = Patron
    context_object_name = "patrons"
    template_name = "patrons/patron_list.html"


class PatronDetailView(DetailView):
    model = Patron
    context_object_name = "patron"
    template_name = "patrons/patron_detail.html"


class PatronCreateView(CreateView):
    model = Patron
    form_class = PatronForm
    success_url = reverse_lazy("patrons:patron_list")


class PatronUpdateView(UpdateView):
    model = Patron
    form_class = PatronForm
    def get_success_url(self):
        return reverse_lazy("patrons:patron_list")


class PatronDeleteView(DeleteView):
    model = Patron
    success_url = reverse_lazy("patrons:patron_list")
