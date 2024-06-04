from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from django.views.generic.edit import (
    CreateView,
    DeleteView,
    UpdateView,
)

from .forms import NotificationForm
from .models import Notification

# Create your views here.


class NotificationListView(ListView):
    model = Notification
    context_object_name = "notifications"
    template_name = "notifications/notification_list.html"


class NotificationDetailView(DetailView):
    model = Notification
    context_object_name = "notification"
    template_name = "notifications/notification_detail.html"


class NotificationCreateView(CreateView):
    model = Notification
    form_class = NotificationForm
    success_url = reverse_lazy("notifications:notification_list")


class NotificationDeleteView(DeleteView):
    model = Notification
    success_url = reverse_lazy("notifications:notification_list")


class NotificationUpdateView(UpdateView):
    model = Notification
    form_class = NotificationForm
    def get_success_url(self):
        return reverse_lazy("notifications:notification_list")
