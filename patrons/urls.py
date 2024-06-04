from django.urls import path
from .views import (
    PatronListView,
    PatronDetailView,
    PatronCreateView,
    PatronDeleteView,
    PatronUpdateView,
)

urlpatterns = [
    path("", PatronListView.as_view(), name="patron_list"),
    path("create/", PatronCreateView.as_view(), name="patron_create"),
    path("<int:pk>/get/", PatronDetailView.as_view(), name="patron_detail"),
    path("<int:pk>/delete/", PatronDeleteView.as_view(), name="patron_delete"),
    path("<int:pk>/edit/", PatronUpdateView.as_view(), name="patron_edit"),
]
