from django.urls import path
from .views import (
    LocationListView,
    LocationDetailView,
    LocationCreateView,
    LocationDeleteView,
    LocationUpdateView,
)

urlpatterns = [
    path("", LocationListView.as_view(), name="location_list"),
    path("create/", LocationCreateView.as_view(), name="location_create"),
    path("<int:pk>/get/", LocationDetailView.as_view(), name="location_detail"),
    path("<int:pk>/delete/", LocationDeleteView.as_view(), name="location_delete"),
    path("<int:pk>/edit/", LocationUpdateView.as_view(), name="location_edit"),
]
