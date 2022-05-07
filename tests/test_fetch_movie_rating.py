from django.test import TestCase
from rating.models import Movie, Rating, User
from django.urls import reverse
from rest_framework.test import APIClient
import json

class TestFetchMovieRatingByName(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.movie = Movie.objects.create(
            name = "Test Movie",
            year = 2022
        )
        self.rating = 3
        self.user = User.objects.create(
            name = "testUser"
        )
        self.rating_obj = Rating.objects.create(
            movie = self.movie,
            user = self.user,
            rating =self.rating
        )
        return super().setUp()
    
    def test_fetchMovieRatingByName(self):
        response = self.client.get(reverse('getMovieRatingByName', kwargs={"movie_title":self.movie.name}))
        self.assertEquals(response.status_code,200)
        json_data = json.loads(response.content)
        count = json_data.get('count')
        data = json_data.get('data')
        self.assertEquals(1, count)
        for i in range(count):
            self.assertEquals(data[i].get('movie_name'), self.movie.name)
            self.assertEquals(data[i].get('rating'), self.rating)
            self.assertEquals(data[i].get('user'),str(self.user.id))


class TestFetchMovieRatingByID(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.movie = Movie.objects.create(
            name = "Test Movie",
            year = 2022
        )
        self.rating = 3
        self.user = User.objects.create(
            name = "testUser"
        )
        self.rating_obj = Rating.objects.create(
            movie = self.movie,
            user = self.user,
            rating =self.rating
        )
        return super().setUp()
    
    def test_fetchMovieRatingById(self):
        response = self.client.get(reverse('getMovieRatingById', kwargs={"movie_id":self.movie.id}))
        self.assertEquals(response.status_code,200)
        json_data = json.loads(response.content)
        count = json_data.get('count')
        data = json_data.get('data')
        self.assertEquals(1, count)
        for i in range(count):
            self.assertEquals(data[i].get('movie_name'), self.movie.name)
            self.assertEquals(data[i].get('rating'), self.rating)
            self.assertEquals(data[i].get('user'),str(self.user.id))

        