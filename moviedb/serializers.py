from typing import SupportsRound
from rest_framework import serializers

from moviedb.models import Movie, Actor, Cast


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            "title",
            "budget",
            "homepage",
            "description",
            "release_date",
            "runtime",
            "movie_cast",
        )
        depth = 1


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ["id"]
        model = Actor
        fields = ("first_name", "last_name", "age", "email")


class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = (
            "movie",
            "actor",
            "role",
        )
