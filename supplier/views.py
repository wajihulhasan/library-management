from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)

from .forms import SupplierForm
from .models import Supplier


class SupplierListView(ListView):
    model = Supplier
    context_object_name = "suppliers"
    template_name = "supplier/supplier_list.html"


class SupplierDetailView(DetailView):
    model = Supplier
    context_object_name = "supplier"


class SupplierCreateView(CreateView):
    model = Supplier
    form_class = SupplierForm
    success_url = reverse_lazy("supplier:supplier_list")


class SupplierUpdateView(UpdateView):
    model = Supplier
    form_class = SupplierForm

    def get_success_url(self):
        return reverse("supplier:supplier_detail", kwargs={"pk": self.object.pk})


class SupplierDeleteView(DeleteView):
    model = Supplier
    success_url = reverse_lazy("supplier:supplier_list")
