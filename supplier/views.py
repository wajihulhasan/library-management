from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, DeleteView,  UpdateView

from .models import UserLog

class UserLogListView(ListView):
    model = UserLog
    context_object_name = 'logs'

class UserLogDetailView(DetailView):
    model = UserLog
    context_object_name = 'log'

class UserLogCreateView(CreateView):
    model = UserLog
    success_url = reverse_lazy('userlog_list')

class UserLogUpdateView(UpdateView):
    model = UserLog
    success_url = reverse_lazy('userlog_list')

class UserLogDeleteView(DeleteView):
    model = UserLog
    success_url = reverse_lazy('userlog_list')


