from django.urls import path
from .views import EventListView, EventDetailView, CreateEventView, DeleteEventView, UpdateEventView

urlpatterns = [
    path("", EventListView.as_view(), name="event_list"),
    path("create/", CreateEventView.as_view(), name="event_create"),
    path("<int:pk>/get/", EventDetailView.as_view(), name="event_detail"),
    path("<int:pk>/delete/", DeleteEventView.as_view(), name="event_delete"),
    path("<int:pk>/edit/", UpdateEventView.as_view(), name="event_edit")
]
