from django.urls import path
from .views import (
    PublisherListView,
    PublisherDetailView,
    PublisherCreateView,
    PublisherDeleteView,
    PublisherUpdateView,
)

urlpatterns = [
    path("", PublisherListView.as_view(), name="publisher_list"),
    path("create/", PublisherCreateView.as_view(), name="publisher_create"),
    path("<int:pk>/get/", PublisherDetailView.as_view(), name="publisher_detail"),
    path("<int:pk>/delete/", PublisherDeleteView.as_view(), name="publisher_delete"),
    path("<int:pk>/edit/", PublisherUpdateView.as_view(), name="publisher_edit"),
]
