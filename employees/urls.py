from django.urls import path
from .views import EmployeeListView, EmployeeDetailView, CreateEmployeeView, DeleteEmployeeView, UpdateEmployeeView

urlpatterns = [
    path("", EmployeeListView.as_view(), name="employee_list"),
    path("create/", CreateEmployeeView.as_view(), name="employee_create"),
    path("<int:pk>/get/", EmployeeDetailView.as_view(), name="employee_detail"),
    path("<int:pk>/delete/", DeleteEmployeeView.as_view(), name="employee_delete"),
    path("<int:pk>/edit/", UpdateEmployeeView.as_view(), name="employee_edit")
]
