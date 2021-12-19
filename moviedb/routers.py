from rest_framework import routers
from moviedb import views

router = routers.DefaultRouter()
router.register(r'movie', views.MovieViewSet, basename='movie')
