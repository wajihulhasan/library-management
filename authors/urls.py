from django.urls import path
from .views import AuthorListView, AuthorDetailView, CreateAuthorView, DeleteAuthorView, UpdateAuthorView

urlpatterns = [
    path("", AuthorListView.as_view(), name="author_list"),
    path("create/", CreateAuthorView.as_view(), name="author_create"),
    path("<int:pk>/get/", AuthorDetailView.as_view(), name="author_detail"),
    path("<int:pk>/delete/", DeleteAuthorView.as_view(), name="author_delete"),
    path("<int:pk>/edit/", UpdateAuthorView.as_view(), name="author_edit")
]


