from django.urls import path
from .views import BookCopyListView, BookCopyDetailView, BookCopyCreateView, BookCopyDeleteView, BookCopyUpdateView

urlpatterns = [
    path("", BookCopyListView.as_view(), name="book_copies_list"),
    path("create/", BookCopyCreateView.as_view(), name="book_copies_create"),
    path("<int:pk>/get/", BookCopyDetailView.as_view(), name="book_copies_detail"),
    path("<int:pk>/delete/", BookCopyDeleteView.as_view(), name="book_copies_delete"),
    path("<int:pk>/edit/", BookCopyUpdateView.as_view(), name="book_copies_edit")
]


