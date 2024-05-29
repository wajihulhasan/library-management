from django.urls import path
from .views import NotificationListView, NotificationDetailView, CreateNotificationView, DeleteNotificationView, UpdateNotificationView

urlpatterns = [
    path("", NotificationListView.as_view(), name="notification_list"),
    path("create/", CreateNotificationView.as_view(), name="notification_create"),
    path("<int:pk>/get/", NotificationDetailView.as_view(), name="notification_detail"),
    path("<int:pk>/delete/", DeleteNotificationView.as_view(), name="notification_delete"),
    path("<int:pk>/edit/", UpdateNotificationView.as_view(), name="notification_edit")
]
