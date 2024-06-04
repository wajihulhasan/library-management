from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    UpdateView,
)

from .forms import DepartmentForm
# Create your views here.
from .models import Department


class DepartmentListView(ListView):
    model = Department
    context_object_name = "departments"
    template_name = "departments/department_list.html"


class DepartmentDetailView(DetailView):
    model = Department
    context_object_name = "department"
    template_name = "departments/department_detail.html"


class DepartmentCreateView(CreateView):
    model = Department
    form_class = DepartmentForm
    success_url = reverse_lazy("departments:department_list")


class DepartmentUpdateView(UpdateView):
    model = Department
    form_class = DepartmentForm
    def get_success_url(self):
        return reverse_lazy("department_list")


class DepartmentDeleteView(DeleteView):
    model = Department
    success_url = reverse_lazy("departments:department_list")
