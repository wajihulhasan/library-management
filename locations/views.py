from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from django.views.generic.edit import (
    CreateView,
    DeleteView,
    UpdateView,
)

from .forms import LocationForm
from .models import Location

# Create your views here.


class LocationListView(ListView):
    model = Location
    context_object_name = "locations"
    template_name = "locations/location_list.html"


class LocationDetailView(DetailView):
    model = Location
    context_object_name = "location"
    template_name = "locations/location_detail.html"


class LocationCreateView(CreateView):
    model = Location
    form_class = LocationForm
    success_url = reverse_lazy("locations:location_list")


class LocationDeleteView(DeleteView):
    model = Location
    success_url = reverse_lazy("locations:location_list")


class LocationUpdateView(UpdateView):
    model = Location
    form_class = LocationForm
    def get_success_url(self):
        return reverse_lazy("locations:location_list")
