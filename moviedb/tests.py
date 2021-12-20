from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status


from moviedb.models import Movie


class MovieTests(APITestCase):
    def test_add_movie(self):
        """
        Ensure we can add a new movie.
        """

        data = {
            "title": "Filme 01",
            "budget": 100000,
            "homepage": "https://www.google.com",
            "description": "Descrição para o filme 01",
            "release_date": "2021-01-01",
            "runtime": 120,
        }

        url = reverse("movie-list")
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 1)
        self.assertEqual(Movie.objects.get().title, "Filme 01")
