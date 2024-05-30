from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, DeleteView,  UpdateView

from .models import Publisher
# Create your views here.

class PublisherListView(ListView):
    model = Publisher
    context_object_name = 'publishers'

class PublisherDetailView(DetailView):
    model = Publisher
    context_object_name = 'publisher'

class PublisherCreateView(CreateView):
    model = Publisher
    success_url = reverse_lazy('publisher_list')

class PublisherUpdateView(UpdateView):
    model = Position
    success_url = reverse_lazy('publisher_list')

class PublisherDeleteView(DeleteView):
    model = Position
    success_url = reverse_lazy('publisher_list')

