from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from django.views.generic.edit import (
    CreateView,
    DeleteView,
    UpdateView,
)

from .forms import PositionForm
from .models import Position

# Create your views here.


class PositionListView(ListView):
    model = Position
    context_object_name = "positions"
    template_name = "positions/position_list.html"


class PositionDetailView(DetailView):
    model = Position
    context_object_name = "position"
    template_name = "positions/position_details.html"


class PositionCreateView(CreateView):
    model = Position
    form_class = PositionForm
    success_url = reverse_lazy("positions:position_list")


class PositionUpdateView(UpdateView):
    model = Position
    form_class = PositionForm
    def get_success_url(self):
        return reverse_lazy("positions:position_list")


class PositionDeleteView(DeleteView):
    model = Position
    success_url = reverse_lazy("positions:position_list")
