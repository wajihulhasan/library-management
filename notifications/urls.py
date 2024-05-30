from django.urls import path
from .views import NotificationListView, NotificationDetailView, NotificationCreateView, NotificationDeleteView, NotificationUpdateView

urlpatterns = [
    path("", NotificationListView.as_view(), name="notification_list"),
    path("create/", NotificationCreateView.as_view(), name="notification_create"),
    path("<int:pk>/get/", NotificationDetailView.as_view(), name="notification_detail"),
    path("<int:pk>/delete/", NotificationDeleteView.as_view(), name="notification_delete"),
    path("<int:pk>/edit/", NotificationUpdateView.as_view(), name="notification_edit")
]
