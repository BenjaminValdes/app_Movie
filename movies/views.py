from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
import datetime

from .models import Movie
from .forms import MovieForm


def get_movies(request):
    movies = Movie.objects.all()
    form = MovieForm(request.POST)
    error = False
    if form.is_valid():
        form.save(commit=True)
    else:
        error = True
    return render(request, 'movie_list.html',
                  context = {'movies': movies,
                            'error': error,
                             'form': form})

@login_required
def movie(request, id_movie):
    movie = Movie.objects.get(pk=id_movie)
    return render(request, 'movie_detail.html',
                 context={'movies': movie})
    