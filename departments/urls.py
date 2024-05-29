from django.urls import path
from .views import DepartmentListView, DepartmentDetailView, CreateDepartmentView, DeleteDepartmentView, UpdateDepartmentView

urlpatterns = [
    path("", DepartmentListView.as_view(), name="department_list"),
    path("create/", CreateDepartmentView.as_view(), name="department_create"),
    path("<int:pk>/get/", DepartmentDetailView.as_view(), name="department_detail"),
    path("<int:pk>/delete/", DeleteDepartmentView.as_view(), name="department_delete"),
    path("<int:pk>/edit/", UpdateDepartmentView.as_view(), name="department_edit")
]
