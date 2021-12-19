from django.contrib import admin
from moviedb.models import Movie

admin.site.site_header = "Movie Database"
admin.site.site_title = "Movie Database Admin Portal"
admin.site.index_title = "Welcome to Movie Database Portal"


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'budget', 'homepage', 'description', 'release_date', 'runtime')