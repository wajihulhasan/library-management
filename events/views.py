from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView,  UpdateView

from .models import Event
# Create your views here.

class EventListView(ListView):
    model = Event
    context_object_name = 'events'

class EventDetailView(DetailView):
    model = Event
    context_object_name = 'event'

class EventCreateView(CreateView):
    model = Event
    success_url = reverse_lazy('event_list')

class EventUpdateView(UpdateView):
    model = Event
    success_url = reverse_lazy('event_detail')

class EventDeleteView(DeleteView):
    model = Event
    success_url = reverse_lazy('event_list')


