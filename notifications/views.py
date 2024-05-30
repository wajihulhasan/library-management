from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, DeleteView,  UpdateView

from .models import Notification
# Create your views here.

class NotificationListView(ListView):
    model = Notification
    context_object_name = 'notifications'

class NotificationDetailView(DetailView):
    model = Notification
    context_object_name = 'notification'

class NotificationCreateView(CreateView):
    model = Notification
    success_url = reverse_lazy('notification_list')

class NotificationDeleteView(DeleteView):
    model = Notification
    success_url = reverse_lazy('notification_list')

class NotificationUpdateView(UpdateView):
    model = Notification
    success_url = reverse_lazy('notification_detail')




