from django.urls import path
from .views import EventRegistrationListView, EventRegistrationDetailView, CreateEventRegistrationView, DeleteEventRegistrationView, UpdateEventRegistrationView

urlpatterns = [
    path("", EventRegistrationListView.as_view(), name="event_registration_list"),
    path("create/", CreateEventRegistrationView.as_view(), name="event_registration_create"),
    path("<int:pk>/get/", EventRegistrationDetailView.as_view(), name="event_registration_detail"),
    path("<int:pk>/delete/", DeleteEventRegistrationView.as_view(), name="event_registration_delete"),
    path("<int:pk>/edit/", UpdateEventRegistrationView.as_view(), name="event_registration_edit")
]
