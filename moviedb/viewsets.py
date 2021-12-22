from rest_framework import viewsets

from rest_framework import permissions

from moviedb.models import Movie, Actor, Cast
from moviedb.serializers import MovieSerializer, ActorSerializer, CastSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint for movies.
    """

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ActorViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Actors.
    """

    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CastViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Cast information.
    """

    queryset = Cast.objects.all()
    serializer_class = CastSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
