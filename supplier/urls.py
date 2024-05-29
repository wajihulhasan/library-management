from django.urls import path
from .views import SupplierListView, SupplierDetailView, CreateSupplierView, DeleteSupplierView, UpdateSupplierView

urlpatterns = [
    path("", SupplierListView.as_view(), name="supplier_list"),
    path("create/", CreateSupplierView.as_view(), name="supplier_create"),
    path("<int:pk>/get/", SupplierDetailView.as_view(), name="supplier_detail"),
    path("<int:pk>/delete/", DeleteSupplierView.as_view(), name="supplier_delete"),
    path("<int:pk>/edit/", UpdateSupplierView.as_view(), name="supplier_edit")
]
