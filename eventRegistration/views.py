from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    UpdateView,
)

from .forms import EventRegistrationForm
from .models import EventRegistration

# Create your views here.


class EventRegistrationListView(ListView):
    model = EventRegistration
    context_object_name = "eventregistrations"
    template_name = "eventRegistration/eventregistration_list.html"


class EventRegistrationDetailView(DetailView):
    model = EventRegistration
    context_object_name = "eventregistration"
    template_name = "eventRegistration/eventregistration_detail.html"


class EventRegistrationCreateView(CreateView):
    model = EventRegistration
    form_class = EventRegistrationForm
    success_url = reverse_lazy("eventRegistration:event_registration_list")


class EventRegistrationDeleteView(DeleteView):
    model = EventRegistration
    success_url = reverse_lazy("eventRegistration:event_registration_list")


class EventRegistrationUpdateView(UpdateView):
    model = EventRegistration
    form_class = EventRegistrationForm
    def get_success_url(self):
        return reverse_lazy("eventRegistration:event_registration_list")


