from django.urls import path
from .views import AuthorListView, AuthorDetailView, CreateAuthorView, DeleteAuthorView, UpdateAuthorView

urlpatterns = [
    path("", AuthorListView.as_view(), name="author_list"),
    path("create/", AuthorCreateView.as_view(), name="author_create"),
    path("<int:pk>/get/", AuthorDetailView.as_view(), name="author_detail"),
    path("<int:pk>/delete/", AuthorDeleteView.as_view(), name="author_delete"),
    path("<int:pk>/edit/", AuthorUpdateView.as_view(), name="author_edit")
]


