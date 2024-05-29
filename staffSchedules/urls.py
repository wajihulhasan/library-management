from django.urls import path
from .views import StaffScheduleListView, StaffScheduleDetailView, CreateStaffScheduleView, DeleteStaffScheduleView, UpdateStaffScheduleView

urlpatterns = [
    path("", StaffScheduleListView.as_view(), name="staff_schedule_list"),
    path("create/", StaffScheduleCreateView.as_view(), name="staff_schedule_create"),
    path("<int:pk>/get/", StaffScheduleDetailView.as_view(), name="staff_schedule_detail"),
    path("<int:pk>/delete/", StaffScheduleDeleteView.as_view(), name="staff_schedule_delete"),
    path("<int:pk>/edit/", StaffScheduleUpdateView.as_view(), name="staff_schedule_edit")
]
