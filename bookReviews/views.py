from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)

from bookReviews.forms import BookReviewForm
from bookReviews.models import BookReview


# Create your views here.
class BookReviewListView(ListView):
    model = BookReview
    context_object_name = "reviews"
    template_name = "bookReviews/bookreview_list.html"



class BookReviewDetailView(DetailView):
    model = BookReview
    context_object_name = "review"
    template_name = "bookReviews/bookreview_detail.html"


class BookReviewCreateView(CreateView):
    model = BookReview
    form_class = BookReviewForm
    success_url = reverse_lazy("bookReviews:book_review_list")


class BookReviewUpdateView(UpdateView):
    model = BookReview
    form_class = BookReviewForm
    def get_success_url(self):
        return reverse_lazy("bookReviews:book_review_list")


class BookReviewDeleteView(DeleteView):
    model = BookReview
    success_url = reverse_lazy("bookReviews:book_review_list")
