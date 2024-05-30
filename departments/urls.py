from django.urls import path
from .views import DepartmentListView, DepartmentDetailView, DepartmentCreateView, DepartmentDeleteView, DepartmentUpdateView

urlpatterns = [
    path("", DepartmentListView.as_view(), name="department_list"),
    path("create/", DepartmentCreateView.as_view(), name="department_create"),
    path("<int:pk>/get/", DepartmentDetailView.as_view(), name="department_detail"),
    path("<int:pk>/delete/", DepartmentDeleteView.as_view(), name="department_delete"),
    path("<int:pk>/edit/", DepartmentUpdateView.as_view(), name="department_edit")
]
