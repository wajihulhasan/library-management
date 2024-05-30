from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, DeleteView,  UpdateView

from .models import StaffSchedule
# Create your views here.

class StaffScheduleListView(ListView):
    model = StaffSchedule
    context_object_name = 'staff_schedules'

class StaffScheduleDetailView(DetailView):
    model = StaffSchedule
    context_object_name = 'staff_schedule'

class StaffScheduleCreateView(CreateView):
    model = StaffSchedule
    success_url = reverse_lazy('staff_schedule_list')

class StaffScheduleUpdateView(UpdateView):
    model = StaffSchedule
    success_url = reverse_lazy('staff_schedule_detail')

class StaffScheduleDeleteView(DeleteView):
    model = StaffSchedule
    success_url = reverse_lazy('staff_schedule_list')


