from django.contrib import admin
from moviedb.models import Movie, Actor, Cast

admin.site.site_header = "Movie Database"
admin.site.site_title = "Movie Database Admin Portal"
admin.site.index_title = "Welcome to Movie Database Portal"


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "budget",
        "homepage",
        "description",
        "release_date",
        "runtime",
    ]


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "age", "email"]


@admin.register(Cast)
class CastAdmin(admin.ModelAdmin):
    list_display = [
        "movie",
        "actor",
        "role",
    ]
