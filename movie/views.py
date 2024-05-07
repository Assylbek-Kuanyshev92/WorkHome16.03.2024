from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from movie.models import Movie



class MoviesView(ListView):
    """Список фильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/movie_list.html"

class MovieDetailView(DetailView):
    """Полное описание фильма"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    slug_field = "url"
from django.shortcuts import render

# Create your views here.
