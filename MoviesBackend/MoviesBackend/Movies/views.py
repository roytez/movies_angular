from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from Movies.models import Movie, Genre, Director, Actor, Music, MovieGenre
from Movies.serializers import MovieSerializer, GenreSerializer, DirectorSerializers, ActorSerializers, MusicSerializers
import random

class MovieViewSet(ViewSet):
    """

    """

    permission_classes = ()
    authentication_classes = ()

    @classmethod
    def list(cls, request):
        return Response({
            "data": MovieSerializer(Movie.objects.all(), many=True).data
        })


class GenreViewSet(ViewSet):
    permission_classes = ()
    authentication_classes = ()

    @classmethod
    def list(cls, request):
        return Response({
            "data": GenreSerializer(Genre.objects.all(), many=True).data
        })


class DirectorViewSet(ViewSet):
    permission_classes = ()
    authentication_classes = ()

    @classmethod
    def list(cls, request):
        return Response({
            "data": DirectorSerializers(Director.objects.all(), many=True).data
        })


class ActorViewSet(ViewSet):
    permission_classes = ()
    authentication_classes = ()

    @classmethod
    def list(cls, request):
        return Response({
            "data": ActorSerializers(Actor.objects.all(), many=True).data
        })


class MusicViewSet(ViewSet):
    permission_classes = ()
    authentication_classes = ()

    @classmethod
    def list(cls, request):
        return Response({
            "data": MusicSerializers(Music.objects.all(), many=True).data
        })


    "funkcja do losowego dodania gatunków do filmów"
    # @classmethod
    # def generate(cls, request):
    #     movies = Movie.objects.all()
    #
    #     genres = Genre.objects.all()
    #
    #     for movie in movies:
    #         random_genre_index = random.randint(0, genres.count() - 1)
    #
    #         movie_genre = MovieGenre()
    #         movie_genre.movie_id = movie.id
    #         movie_genre.genre_id = genres[random_genre_index].id
    #         movie_genre.save()
    #
    #     return Response(dict(
    #         success=True
    #     ))

