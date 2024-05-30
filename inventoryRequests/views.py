from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView,  UpdateView

from .models import InventoryRequest
# Create your views here.

class InventoryRequestListView(ListView):
    model = InventoryRequest
    context_object_name = 'inventory_requests'

class InventoryRequestDetailView(DetailView):
    model = InventoryRequest
    context_object_name = 'inventory_request'

class InventoryRequestCreateView(CreateView):
    model = InventoryRequest
    success_url = reverse_lazy('inventory_request_list')

class InventoryRequestDeleteView(DeleteView):
    model = InventoryRequest
    success_url = reverse_lazy('inventory_request_list')

class InventoryRequestUpdateView(UpdateView):
    model = InventoryRequest
    success_url = reverse_lazy('inventory_request_detail')

