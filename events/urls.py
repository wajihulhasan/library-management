from django.urls import path
from .views import (
    EventListView,
    EventDetailView,
    EventCreateView,
    EventDeleteView,
    EventUpdateView,
)

urlpatterns = [
    path("", EventListView.as_view(), name="event_list"),
    path("create/", EventCreateView.as_view(), name="event_create"),
    path("<int:pk>/get/", EventDetailView.as_view(), name="event_detail"),
    path("<int:pk>/delete/", EventDeleteView.as_view(), name="event_delete"),
    path("<int:pk>/edit/", EventUpdateView.as_view(), name="event_edit"),
]
