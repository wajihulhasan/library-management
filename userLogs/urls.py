from django.urls import path
from .views import UserLogListView, UserLogDetailView, CreateUserLogView, DeleteUserLogView, UpdateUserLogView

urlpatterns = [
    path("", UserLogListView.as_view(), name="user_log_list"),
    path("create/", CreateUserLogView.as_view(), name="user_log_create"),
    path("<int:pk>/get/", UserLogDetailView.as_view(), name="user_log_detail"),
    path("<int:pk>/delete/", DeleteUserLogView.as_view(), name="user_log_delete"),
    path("<int:pk>/edit/", UpdateUserLogView.as_view(), name="user_log_edit")
]
