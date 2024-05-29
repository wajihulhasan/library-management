from django.urls import path
from .views import PositionListView, PositionDetailView, CreatePositionView, DeletePositionView, UpdatePositionView

urlpatterns = [
    path("", PositionListView.as_view(), name="position_list"),
    path("create/", PositionCreateView.as_view(), name="position_create"),
    path("<int:pk>/get/", PositionDetailView.as_view(), name="position_detail"),
    path("<int:pk>/delete/", PositionDeleteView.as_view(), name="position_delete"),
    path("<int:pk>/edit/", PositionUpdateView.as_view(), name="position_edit")
]
