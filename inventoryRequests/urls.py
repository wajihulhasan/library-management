from django.urls import path
from .views import InventoryRequestListView, InventoryRequestDetailView, InventoryRequestCreateView, InventoryRequestDeleteView, InventoryRequestUpdateView

urlpatterns = [
    path("", InventoryRequestListView.as_view(), name="inventory_request_list"),
    path("create/", InventoryRequestCreateView.as_view(), name="inventory_request_create"),
    path("<int:pk>/get/", InventoryRequestDetailView.as_view(), name="inventory_request_detail"),
    path("<int:pk>/delete/", InventoryRequestDeleteView.as_view(), name="inventory_request_delete"),
    path("<int:pk>/edit/", InventoryRequestUpdateView.as_view(), name="inventory_request_edit")
]
