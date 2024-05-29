from django.urls import path
from .views import LocationListView, LocationDetailView, CreateLocationView, DeleteLocationView, UpdateLocationView

urlpatterns = [
    path("", LocationListView.as_view(), name="location_list"),
    path("create/", CreateLocationView.as_view(), name="location_create"),
    path("<int:pk>/get/", LocationDetailView.as_view(), name="location_detail"),
    path("<int:pk>/delete/", DeleteLocationView.as_view(), name="location_delete"),
    path("<int:pk>/edit/", UpdateLocationView.as_view(), name="location_edit")
]
