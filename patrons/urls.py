from django.urls import path
from .views import PatronListView, PatronDetailView, CreatePatronView, DeletePatronView, UpdatePatronView

urlpatterns = [
    path("", PatronListView.as_view(), name="patron_list"),
    path("create/", CreatePatronView.as_view(), name="patron_create"),
    path("<int:pk>/get/", PatronDetailView.as_view(), name="patron_detail"),
    path("<int:pk>/delete/", DeletePatronView.as_view(), name="patron_delete"),
    path("<int:pk>/edit/", UpdatePatronView.as_view(), name="patron_edit")
]
