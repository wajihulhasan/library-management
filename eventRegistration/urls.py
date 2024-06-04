from django.urls import path
from .views import (
    EventRegistrationListView,
    EventRegistrationDetailView,
    EventRegistrationCreateView,
    EventRegistrationDeleteView,
    EventRegistrationUpdateView,
)

urlpatterns = [
    path("", EventRegistrationListView.as_view(), name="event_registration_list"),
    path(
        "create/",
        EventRegistrationCreateView.as_view(),
        name="event_registration_create",
    ),
    path(
        "<int:pk>/get/",
        EventRegistrationDetailView.as_view(),
        name="event_registration_detail",
    ),
    path(
        "<int:pk>/delete/",
        EventRegistrationDeleteView.as_view(),
        name="event_registration_delete",
    ),
    path(
        "<int:pk>/edit/",
        EventRegistrationUpdateView.as_view(),
        name="event_registration_edit",
    ),
]
