from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import (
    CreateView,
    DeleteView,
    UpdateView, ListView, DetailView,
)

from .forms import ReservationForm
from .models import Reservation

# Create your views here.


class ReservationListView(ListView):
    model = Reservation
    context_object_name = "reservations"
    template_name = "reservations/reservation_list.html"


class ReservationDetailView(DetailView):
    model = Reservation
    context_object_name = "reservation"
    template_name = "reservations/reservation_detail.html"


class ReservationCreateView(CreateView):
    model = Reservation
    form_class = ReservationForm
    success_url = reverse_lazy("reservations:reservation_list")



class ReservationDeleteView(DeleteView):
    model = Reservation
    success_url = reverse_lazy("reservations:reservation_list")


class ReservationUpdateView(UpdateView):
    model = Reservation
    form_class = ReservationForm
    def get_success_url(self):
        return reverse_lazy("reservations:reservation_list")
