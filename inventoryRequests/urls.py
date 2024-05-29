from django.urls import path
from .views import InventoryRequestListView, InventoryRequestDetailView, CreateInventoryRequestView, DeleteInventoryRequestView, UpdateInventoryRequestView

urlpatterns = [
    path("", InventoryRequestListView.as_view(), name="inventory_request_list"),
    path("create/", InventoryRequestCreateView.as_view(), name="inventory_request_create"),
    path("<int:pk>/get/", InventoryRequestDetailView.as_view(), name="inventory_request_detail"),
    path("<int:pk>/delete/", InventoryRequestDeleteView.as_view(), name="inventory_request_delete"),
    path("<int:pk>/edit/", InventoryRequesUpdatetView.as_view(), name="inventory_request_edit")
]
