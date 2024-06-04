from django.urls import path
from .views import (
    FineListView,
    FineDetailView,
    FineCreateView,
    FineDeleteView,
    FineUpdateView,
)

urlpatterns = [
    path("", FineListView.as_view(), name="fine_list"),
    path("create/", FineCreateView.as_view(), name="fine_create"),
    path("<int:pk>/get/", FineDetailView.as_view(), name="fine_detail"),
    path("<int:pk>/delete/", FineDeleteView.as_view(), name="fine_delete"),
    path("<int:pk>/edit/", FineUpdateView.as_view(), name="fine_edit"),
]
