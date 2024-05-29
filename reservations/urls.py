from django.urls import path
from .views import ReservationListView, ReservationDetailView, CreateReservationView, DeleteReservationView, UpdateReservationView

urlpatterns = [
    path("", ReservationListView.as_view(), name="reservation_list"),
    path("create/", ReservationCreateView.as_view(), name="reservation_create"),
    path("<int:pk>/get/", ReservationDetailView.as_view(), name="reservation_detail"),
    path("<int:pk>/delete/", ReservationDeleteView.as_view(), name="reservation_delete"),
    path("<int:pk>/edit/", ReservationUpdateView.as_view(), name="reservation_edit")
]
