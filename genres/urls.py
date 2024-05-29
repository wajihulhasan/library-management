from django.urls import path
from .views import GenreListView, GenreDetailView, CreateGenreView, DeleteGenreView, UpdateGenreView

urlpatterns = [
    path("", GenreListView.as_view(), name="genre_list"),
    path("create/", CreateGenreView.as_view(), name="genre_create"),
    path("<int:pk>/get/", GenreDetailView.as_view(), name="genre_detail"),
    path("<int:pk>/delete/", DeleteGenreView.as_view(), name="genre_delete"),
    path("<int:pk>/edit/", UpdateGenreView.as_view(), name="genre_edit")
]
