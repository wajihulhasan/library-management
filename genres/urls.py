from django.urls import path
from .views import GenreListView, GenreCreateView, GenreDeleteView, GenreUpdateView, GenreDetailView


class DetailGenreView:
    pass


urlpatterns = [
    path("", GenreListView.as_view(), name="genre_list"),
    path("create/", GenreCreateView.as_view(), name="genre_create"),
    path("<int:pk>/get/", GenreDetailView.as_view(), name="genre_detail"),
    path("<int:pk>/delete/", GenreDeleteView.as_view(), name="genre_delete"),
    path("<int:pk>/edit/", GenreUpdateView.as_view(), name="genre_edit")
]
