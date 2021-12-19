from rest_framework import viewsets
# from rest_framework import permissions

from moviedb.models import Movie
from moviedb.serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint for movies.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
