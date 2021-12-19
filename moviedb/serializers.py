from rest_framework import serializers
from moviedb.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'title',
            'budget',
            'homepage',
            'description',
            'release_date',
            'runtime',
        )
