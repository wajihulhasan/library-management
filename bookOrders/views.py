from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)

from bookOrders.forms import BookOrderForm
from bookOrders.models import BookOrder


# Create your views here.


class BookOrderListView(ListView):
    model = BookOrder
    context_object_name = "book_orders"
    template_name = "bookOrders/bookorder_list.html"


class BookOrderDetailView(DetailView):
    model = BookOrder
    context_object_name = "book_order"
    template_name = "bookOrders/bookorder_detail.html"


class BookOrderCreateView(CreateView):
    model = BookOrder
    form_class = BookOrderForm
    success_url = reverse_lazy("bookOrders:book_order_list")


class BookOrderUpdateView(UpdateView):
    model = BookOrder
    form_class = BookOrderForm

    def get_success_url(self):
        return reverse("bookOrders:book_order_detail", kwargs={"pk": self.object.pk})


class BookOrderDeleteView(DeleteView):
    model = BookOrder
    success_url = reverse_lazy("bookOrders:book_order_list")
