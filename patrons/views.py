from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, DeleteView,  UpdateView

from .models import Patron
# Create your views here.

class PatronListView(ListView):
    model = Patron
    context_object_name = 'patrons'

class PatronDetailView(DetailView):
    model = Patron
    context_object_name = 'patron'

class PatronCreateView(CreateView):
    model = Patron
    success_url = reverse_lazy('patron_list')

class PatronUpdateView(UpdateView):
    model = Patron
    success_url = reverse_lazy('patron_detail')

class PatronDeleteView(DeleteView):
    model = Patron
    success_url = reverse_lazy('patron_list')


