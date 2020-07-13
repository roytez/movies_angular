from django.contrib import admin

# Register your models here.
from Movies.models import Movie, Genre


class MovieAdmin(admin.ModelAdmin):
    pass


class GenreAdmin(admin.ModelAdmin):
    pass


admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)
