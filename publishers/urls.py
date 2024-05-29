from django.urls import path
from .views import PublisherListView, PublisherDetailView, CreatePublisherView, DeletePublisherView, UpdatePublisherView

urlpatterns = [
    path("", PublisherListView.as_view(), name="publisher_list"),
    path("create/", CreatePublisherView.as_view(), name="publisher_create"),
    path("<int:pk>/get/", PublisherDetailView.as_view(), name="publisher_detail"),
    path("<int:pk>/delete/", DeletePublisherView.as_view(), name="publisher_delete"),
    path("<int:pk>/edit/", UpdatePublisherView.as_view(), name="publisher_edit")
]
