from django.urls import path
from .views import EmployeeListView, EmployeeDetailView, EmployeeCreateView, EmployeeDeleteView, EmployeeUpdateView

urlpatterns = [
    path("", EmployeeListView.as_view(), name="employee_list"),
    path("create/", EmployeeCreateView.as_view(), name="employee_create"),
    path("<int:pk>/get/", EmployeeDetailView.as_view(), name="employee_detail"),
    path("<int:pk>/delete/", EmployeeDeleteView.as_view(), name="employee_delete"),
    path("<int:pk>/edit/", EmployeeUpdateView.as_view(), name="employee_edit")
]
