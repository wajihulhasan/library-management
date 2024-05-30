from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView,  UpdateView

from .models import Loan
# Create your views here.

class LoanListView(ListView):
    model = Loan
    context_object_name = 'loans'

class LoanDetailView(DetailView):
    model = Loan
    context_object_name = 'loan'

class LoanCreateView(CreateView):
    model = Loan
    success_url = reverse_lazy('loan_list')

class LoanDeleteView(DeleteView):
    model = Loan
    success_url = reverse_lazy('loan_list')

class LoanUpdateView(UpdateView):
    model = Loan
    success_url = reverse_lazy('loan_list')

