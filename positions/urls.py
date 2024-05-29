from django.urls import path
from .views import PositionListView, PositionDetailView, CreatePositionView, DeletePositionView, UpdatePositionView

urlpatterns = [
    path("", PositionListView.as_view(), name="position_list"),
    path("create/", CreatePositionView.as_view(), name="position_create"),
    path("<int:pk>/get/", PositionDetailView.as_view(), name="position_detail"),
    path("<int:pk>/delete/", DeletePositionView.as_view(), name="position_delete"),
    path("<int:pk>/edit/", UpdatePositionView.as_view(), name="position_edit")
]
