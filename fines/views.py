from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView,  UpdateView

from .models import Fine
# Create your views here.

class FineListView(ListView):
    model = Fine
    context_object_name = 'fines'

class FineDetailView(DetailView):
    model = Fine
    context_object_name = 'fine'

class FineCreateView(CreateView):
    model = Fine
    success_url = reverse_lazy('fine_list')

class FineUpdateView(UpdateView):
    model = Fine
    success_url = reverse_lazy('fine_detail')

class FineDeleteView(DeleteView):
    model = Fine
    success_url = reverse_lazy('fine_list')

