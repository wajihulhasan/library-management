from django.urls import path
from .views import BookListView, BookDetailView, CreateBookView, DeleteBookView, UpdateBookView

urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("create/", CreateBookView.as_view(), name="book_create"),
    path("<int:pk>/get/", BookDetailView.as_view(), name="book_detail"),
    path("<int:pk>/delete/", DeleteBookView.as_view(), name="book_delete"),
    path("<int:pk>/edit/", UpdateBookView.as_view(), name="book_edit")
]
