from django.urls import path
from .views import BookReviewListView, BookReviewDetailView, CreateBookReviewView, DeleteBookReviewView, UpdateBookReviewView

urlpatterns = [
    path("", BookReviewListView.as_view(), name="book_review_list"),
    path("create/", CreateBookReviewView.as_view(), name="book_review_create"),
    path("<int:pk>/get/", BookReviewDetailView.as_view(), name="book_review_detail"),
    path("<int:pk>/delete/", DeleteBookReviewView.as_view(), name="book_review_delete"),
    path("<int:pk>/edit/", UpdateBookReviewView.as_view(), name="book_review_edit")
]


