from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, DeleteView,  UpdateView

from .models import Reservation
# Create your views here.

class ReservationListView(ListView):
    model = Reservation
    context_object_name = 'reservations'

class ReservationDetailView(DetailView):
    model = Reservation
    context_object_name = 'reservation'

class ReservationCreateView(CreateView):
    model = Reservation
    success_url = reverse_lazy('reservation_list')

class ReservationDeleteView(DeleteView):
    model = Reservation
    success_url = reverse_lazy('reservation_list')

class ReservationUpdateView(UpdateView):
    model = Reservation
    success_url = reverse_lazy('reservation_detail')

