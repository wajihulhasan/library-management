from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, DeleteView,  UpdateView

from .models import Position
# Create your views here.

class PositionListView(ListView):
    model = Position
    context_object_name = 'positions'

class PositionDetailView(DetailView):
    model = Position
    context_object_name = 'position'

class PositionCreateView(CreateView):
    model = Position
    success_url = reverse_lazy('position_list')

class PositionUpdateView(UpdateView):
    model = Position
    success_url = reverse_lazy('position_list')

class PositionDeleteView(DeleteView):
    model = Position
    success_url = reverse_lazy('position_list')


