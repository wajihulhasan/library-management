from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookDeleteView,
    BookUpdateView,
)

urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("create/", BookCreateView.as_view(), name="book_create"),
    path("<int:pk>/get/", BookDetailView.as_view(), name="book_detail"),
    path("<int:pk>/delete/", BookDeleteView.as_view(), name="book_delete"),
    path("<int:pk>/edit/", BookUpdateView.as_view(), name="book_edit"),
]
