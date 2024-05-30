from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, DeleteView,  UpdateView

from .models import Supplier

class SupplierListView(ListView):
    model = Supplier
    context_object_name = 'suppliers'

class SupplierDetailView(DetailView):
    model = Supplier
    context_object_name = 'supplier'

class SupplierCreateView(CreateView):
    model = Supplier
    success_url = reverse_lazy('supplier_list')

class SupplierUpdateView(UpdateView):
    model = Supplier
    success_url = reverse_lazy('supplier_detail')

class SupplierDeleteView(DeleteView):
    model = Supplier
    success_url = reverse_lazy('supplier_list')




