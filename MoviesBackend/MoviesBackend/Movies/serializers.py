from rest_framework import serializers

from Movies.models import Movie, MovieGenre, Genre, Director, Actor, Music


class MovieGenreSerializer(serializers.ModelSerializer):
    genre_name = serializers.ReadOnlyField(source='genre.name')
    movie_title = serializers.ReadOnlyField(source='movie.title')
    id = serializers.ReadOnlyField(source='genre.id')

    class Meta:
        model = MovieGenre
        fields = ['genre_name', 'movie_title', 'id']


class MovieSerializer(serializers.ModelSerializer):
    genres = MovieGenreSerializer(source='movie_genres', many=True)

    class Meta:
        model = Movie
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    # genre_name = Movie

    class Meta:
        model = Genre
        fields = '__all__'


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class ActorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class MusicSerializers(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'
