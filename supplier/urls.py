from django.urls import path
from .views import SupplierListView, SupplierDetailView, SupplierCreateView, SupplierDeleteView, SupplierUpdateView

urlpatterns = [
    path("", SupplierListView.as_view(), name="supplier_list"),
    path("create/", SupplierCreateView.as_view(), name="supplier_create"),
    path("<int:pk>/get/", SupplierDetailView.as_view(), name="supplier_detail"),
    path("<int:pk>/delete/", SupplierDeleteView.as_view(), name="supplier_delete"),
    path("<int:pk>/edit/", SupplierUpdateView.as_view(), name="supplier_edit")
]
