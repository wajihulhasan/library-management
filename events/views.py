from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    UpdateView,
)

from .forms import EventForm
from .models import Event

# Create your views here.


class EventListView(ListView):
    model = Event
    context_object_name = "events"
    template_name = "events/event_list.html"


class EventDetailView(DetailView):
    model = Event
    context_object_name = "event"
    template_name = "events/event_detail.html"


class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy("events:event_list")


class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    def get_success_url(self):
        return reverse_lazy("events:event_list")


class EventDeleteView(DeleteView):
    model = Event
    success_url = reverse_lazy("events:event_list")
