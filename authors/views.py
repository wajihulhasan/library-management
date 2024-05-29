from django.shortcuts import render
from django.views.generic import ListView

from authors.models import Author


# Create your views here.
class AuthorViewList(ListView):
    model = Author

