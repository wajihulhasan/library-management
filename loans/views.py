from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    UpdateView,
)

from .forms import LoanForm
from .models import Loan

# Create your views here.


class LoanListView(ListView):
    model = Loan
    context_object_name = "loans"
    template_name = "loans/loan_list.html"


class LoanDetailView(DetailView):
    model = Loan
    context_object_name = "loan"
    template_name = "loans/loan_detail.html"


class LoanCreateView(CreateView):
    model = Loan
    form_class = LoanForm
    success_url = reverse_lazy("loans:loan_list")


class LoanDeleteView(DeleteView):
    model = Loan
    success_url = reverse_lazy("loans:loan_list")


class LoanUpdateView(UpdateView):
    model = Loan
    form_class = LoanForm
    def get_success_url(self):
        return reverse_lazy("loans:loan_list")
