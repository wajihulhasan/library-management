from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    UpdateView,
)

from .forms import InventoryRequestForm
from .models import InventoryRequest

# Create your views here.


class InventoryRequestListView(ListView):
    model = InventoryRequest
    context_object_name = "inventory_requests"
    template_name = "inventoryRequests/inventoryrequest_list.html"


class InventoryRequestDetailView(DetailView):
    model = InventoryRequest
    context_object_name = "inventory_request"
    template_name = "inventoryRequests/inventoryrequest_detail.html"


class InventoryRequestCreateView(CreateView):
    model = InventoryRequest
    form_class = InventoryRequestForm
    success_url = reverse_lazy("inventoryRequests:inventory_request_list")


class InventoryRequestDeleteView(DeleteView):
    model = InventoryRequest
    success_url = reverse_lazy("inventoryRequests:inventory_request_list")


class InventoryRequestUpdateView(UpdateView):
    model = InventoryRequest
    form_class = InventoryRequestForm
    def get_success_url(self):
        return reverse_lazy("inventoryRequests:inventory_request_list")
