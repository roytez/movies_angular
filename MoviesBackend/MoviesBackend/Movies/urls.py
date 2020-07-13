from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns

from Movies.views import MovieViewSet, GenreViewSet, DirectorViewSet, ActorViewSet, MusicViewSet

movie_list = MovieViewSet.as_view({
    'get': 'list'
})

genre_list = GenreViewSet.as_view({
    'get': 'list'
})

director_list = DirectorViewSet.as_view({
    'get': 'list'
})

actor_list = ActorViewSet.as_view({
    'get': 'list'
})

music_list = MusicViewSet.as_view({
    'get': 'list'
})

generate_list = MusicViewSet.as_view({
    'get': 'generate'
})

urlpatterns = format_suffix_patterns([
    re_path('movies', movie_list, name='movie_list'),
    re_path('genres', genre_list, name='genre_list'),
    re_path('directors', director_list, name='director_list'),
    re_path('actors', actor_list, name='actor_list'),
    re_path('music', music_list, name='music_list'),
    re_path('generate', generate_list, name='generate_list'),
])
