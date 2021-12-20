from rest_framework import routers
from moviedb import viewsets

router = routers.DefaultRouter()
router.register("movie", viewsets.MovieViewSet, basename="movie")
router.register("actor", viewsets.ActorViewSet, basename="actor")
router.register("cast", viewsets.CastViewSet, basename="cast")
