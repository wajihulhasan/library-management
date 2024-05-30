from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView,  UpdateView
# Create your views here.
from .models import Department

class DepartmentListView(ListView):
    model = Department
    context_object_name = 'departments'

class DepartmentDetailView(DetailView):
    model = Department
    context_object_name = 'department'

class DepartmentCreateView(CreateView):
    model = Department
    success_url = reverse_lazy('department_list')

class DepartmentUpdateView(UpdateView):
    model = Department
    success_url = reverse_lazy('department_detail')

class DepartmentDeleteView(DeleteView):
    model = Department
    success_url = reverse_lazy('department_list')


