from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView

from django.views.generic.edit import (
    CreateView,
    DeleteView,
    UpdateView,
)

from positions.models import Position
from .forms import PublisherForm
from .models import Publisher

# Create your views here.


class PublisherListView(ListView):
    model = Publisher
    context_object_name = "publishers"
    template_name = "publishers/publishers_list.html"


class PublisherDetailView(DetailView):
    model = Publisher
    context_object_name = "publisher"


class PublisherCreateView(CreateView):
    model = Publisher
    form_class = PublisherForm
    success_url = reverse_lazy("publishers:publisher_list")


class PublisherUpdateView(UpdateView):
    model = Publisher
    form_class = PublisherForm

    def get_success_url(self):
        return reverse("publishers:publisher_detail", kwargs={"pk": self.object.pk})


class PublisherDeleteView(DeleteView):
    model = Publisher
    success_url = reverse_lazy("publishers:publisher_list")
