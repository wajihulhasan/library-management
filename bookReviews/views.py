from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
class BookReviewListView(ListView):
    model = BookReview
    context_object_name = 'reviews'

class BookReviewDetailView(DetailView):
    model = BookReview
    context_object_name = 'review'

class BookReviewCreateView(CreateView):
    model = BookReview
    fields = '__all__'
    success_url = reverse_lazy('book_review_list')

class BookReviewUpdateView(UpdateView):
    model = BookReview
    fields = '__all__'
    success_url = reverse_lazy('book_review_list')

class BookReviewDeleteView(DeleteView):
    model = BookReview
    success_url = reverse_lazy('book_review_list')

