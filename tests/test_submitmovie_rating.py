from django.test import TestCase
from rating.models import Movie, User
from django.urls import reverse
from rest_framework.test import APIClient
import json


class TestSubmitMovieRatingByName(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.movie = Movie.objects.create(name="Test Movie", year=2022)
        self.rating = 3
        return super().setUp()

    def test_submitMovieRatingByName(self):
        response = self.client.post(
            f"/rating/give_rating_by_name/{self.movie.name}/testUser/{self.rating}"
        )
        json_data = json.loads(response.content).get("data")
        self.assertEquals(response.status_code, 200)
        self.assertEquals(json_data.get("movie_name"), self.movie.name)
        self.assertEquals(json_data.get("rating"), self.rating)


class TestSubmitMovieRatingByID(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.movie = Movie.objects.create(name="Test Movie", year=2022)
        self.user = User.objects.create(name="testUser")
        self.rating = 3
        return super().setUp()

    def test_submitMovieRatingById(self):
        response = self.client.post(
            f"/rating/give_rating_by_id/{self.movie.id}/{self.user.id}/{self.rating}"
        )
        json_data = json.loads(response.content).get("data")
        self.assertEquals(response.status_code, 200)
        self.assertEquals(json_data.get("movie_name"), self.movie.name)
        self.assertEquals(json_data.get("rating"), self.rating)
