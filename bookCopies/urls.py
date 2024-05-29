from django.urls import path
from .views import BookCopyListView, BookCopyDetailView, CreateBookCopyView, DeleteBookCopyView, UpdateBookCopyView

urlpatterns = [
    path("", BookCopyListView.as_view(), name="book_copies_list"),
    path("create/", CreateBookCopyView.as_view(), name="book_copies_create"),
    path("<int:pk>/get/", BookCopyDetailView.as_view(), name="book_copies_detail"),
    path("<int:pk>/delete/", DeleteBookCopyView.as_view(), name="book_copies_delete"),
    path("<int:pk>/edit/", UpdateBookCopyView.as_view(), name="book_copies_edit")
]


