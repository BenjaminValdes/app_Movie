from django.contrib import admin
from django.urls import path

from .views import get_movies, movie

urlpatterns = [
    path('<int:id_movie>', movie),
    path('', get_movies),
]
