from django.urls import path
from .views import FineListView, FineDetailView, CreateFineView, DeleteFineView, UpdateFineView

urlpatterns = [
    path("", FineListView.as_view(), name="fine_list"),
    path("create/", CreateFineView.as_view(), name="fine_create"),
    path("<int:pk>/get/", FineDetailView.as_view(), name="fine_detail"),
    path("<int:pk>/delete/", DeleteFineView.as_view(), name="fine_delete"),
    path("<int:pk>/edit/", UpdateFineView.as_view(), name="fine_edit")
]
