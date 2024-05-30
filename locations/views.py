from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, DeleteView,  UpdateView

from .models import Location
# Create your views here.

class LocationListView(ListView):
    model = Location
    context_object_name = 'locations'

class LocationDetailView(DetailView):
    model = Location
    context_object_name = 'location'

class LocationCreateView(CreateView):
    model = Location
    success_url = reverse_lazy('location_list')

class LocationDeleteView(DeleteView):
    model = Location
    success_url = reverse_lazy('location_list')

class LocationUpdateView(UpdateView):
    model = Location
    success_url = reverse_lazy('location_list')


