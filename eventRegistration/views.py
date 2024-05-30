from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView,  UpdateView

from .models import EventRegistration
# Create your views here.

class EventRegistrationListView(ListView):
    model = EventRegistration
    context_object_name = 'eventregistrations'

class EventRegistrationDetailView(DetailView):
    model = EventRegistration
    context_object_name = 'eventregistration'

class EventRegistrationCreateView(CreateView):
    model = EventRegistration
    success_url = reverse_lazy('event_registration_list')

class EventRegistrationDeleteView(DeleteView):
    model = EventRegistration
    success_url = reverse_lazy('event_registration_list')

class EventRegistrationUpdateView(UpdateView):
    model = EventRegistration
    success_url = reverse_lazy('event_registration_detail')
