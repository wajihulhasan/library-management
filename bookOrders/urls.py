from django.urls import path
from .views import BookOrderListView, BookOrderDetailView, CreateBookOrderView, DeleteBookOrderView, UpdateBookOrderView

urlpatterns = [
    path("", BookOrderListView.as_view(), name="book_order_list"),
    path("create/", BookOrderCreateView.as_view(), name="book_order_create"),
    path("<int:pk>/get/", BookOrderDetailView.as_view(), name="book_order_detail"),
    path("<int:pk>/delete/", BookOrderDeleteView.as_view(), name="book_order_delete"),
    path("<int:pk>/edit/", BookOrderUpdateView.as_view(), name="book_order_edit")
]


