from django.urls import path
from .views import UserLogListView, UserLogDetailView, UserLogCreateView, UserLogDeleteView, UserLogUpdateView

urlpatterns = [
    path("", UserLogListView.as_view(), name="user_log_list"),
    path("create/", UserLogCreateView.as_view(), name="user_log_create"),
    path("<int:pk>/get/", UserLogDetailView.as_view(), name="user_log_detail"),
    path("<int:pk>/delete/", UserLogDeleteView.as_view(), name="user_log_delete"),
    path("<int:pk>/edit/", UserLogUpdateView.as_view(), name="user_log_edit")
]
