from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView,  UpdateView

from .models import Employee

# Create your views here.

class EmployeeListView(ListView):
    model = Employee
    context_object_name = 'employees'

class EmployeeDetailView(DetailView):
    model = Employee
    context_object_name = 'employee'

class EmployeeCreateView(CreateView):
    model = Employee
    success_url = reverse_lazy('employee_list')

class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy('employee_list')

class EmployeeUpdateView(UpdateView):
    model = Employee
    success_url = reverse_lazy('employee_detail')

