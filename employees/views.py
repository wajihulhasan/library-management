from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    UpdateView,
)

from .forms import EmployeeForm
from .models import Employee

# Create your views here.


class EmployeeListView(ListView):
    model = Employee
    context_object_name = "employees"
    template_name = "employees/employee_list.html"


class EmployeeDetailView(DetailView):
    model = Employee
    context_object_name = "employee"
    template_name = "employees/employee_detail.html"


class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy("employees:employee_list")


class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy("employees:employee_list")


class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    def get_success_url(self):
        return reverse_lazy("employees:employee_list")
