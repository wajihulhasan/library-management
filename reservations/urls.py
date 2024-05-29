from django.urls import path
from .views import ReservationListView, ReservationDetailView, CreateReservationView, DeleteReservationView, UpdateReservationView

urlpatterns = [
    path("", ReservationListView.as_view(), name="reservation_list"),
    path("create/", CreateReservationView.as_view(), name="reservation_create"),
    path("<int:pk>/get/", ReservationDetailView.as_view(), name="reservation_detail"),
    path("<int:pk>/delete/", DeleteReservationView.as_view(), name="reservation_delete"),
    path("<int:pk>/edit/", UpdateReservationView.as_view(), name="reservation_edit")
]
