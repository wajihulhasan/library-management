from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    UpdateView,
)

from .forms import FineForm
from .models import Fine

# Create your views here.


class FineListView(ListView):
    model = Fine
    context_object_name = "fines"
    template_name = "fines/fine_list.html"


class FineDetailView(DetailView):
    model = Fine
    context_object_name = "fine"
    template_name = "fines/fine_detail.html"


class FineCreateView(CreateView):
    model = Fine
    form_class = FineForm
    success_url = reverse_lazy("fines:fine_list")


class FineUpdateView(UpdateView):
    model = Fine
    form_class = FineForm
    def get_success_url(self):
        return reverse_lazy("fines:fine_list")



class FineDeleteView(DeleteView):
    model = Fine
    success_url = reverse_lazy("fines:fine_list")
