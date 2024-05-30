from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.

class BookOrderListView(ListView):
    model = BookOrder
    context_object_name = 'book_orders'

class BookOrderDetailView(DetailView):
    model = BookOrder
    context_object_name = 'book_order'

class BookOrderCreateView(CreateView):
    model = BookOrder
    success_url = reverse_lazy('book_order_list')

class BookOrderUpdateView(UpdateView):
    model = BookOrder
    success_url = reverse_lazy('book_order_list')

class BookOrderDeleteView(DeleteView):
    model = BookOrder
    success_url = reverse_lazy('book_order_list')
