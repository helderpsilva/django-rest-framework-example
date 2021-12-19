from rest_framework import routers
from moviedb import viewsets

router = routers.DefaultRouter()
router.register(r'movie', viewsets.MovieViewSet, basename='movie')
