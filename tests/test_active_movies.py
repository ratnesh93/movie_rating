from django.test import TestCase
from rating.models import Movie, Rating, User, Onscreen
from django.urls import reverse
from rest_framework.test import APIClient
import json

class TestActiveMovies(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.pincode = 110001
        self.movie = Movie.objects.create(
            name = "testMovie",
            year = "2022"
        )
        self.onScreen = Onscreen.objects.create(
            pincode = self.pincode,
            movie = self.movie
        )
        self.movie2 = Movie.objects.create(
            name = "testMovie2",
            year = "2022"
        )
        self.onScreen2 = Onscreen.objects.create(
            pincode = self.pincode,
            movie = self.movie2
        )
        return super().setUp()
    
    def test_fetch_active_movies_by_pincode(self):
        response = self.client.get(reverse('onScreenApiView', kwargs={"pincode":self.pincode}))
        self.assertEquals(response.status_code,200)
        json_data = json.loads(response.content)
        self.assertEquals(2, json_data.get("count"))
        data = json_data.get('data')
        self.assertEquals(data[0].get('pincode'), self.pincode)
        self.assertEquals(data[0].get('movie_name'), self.movie.name)
        self.assertEquals(data[0].get('movie'), str(self.movie.id))
        self.assertEquals(data[0].get('status'), "active")
        self.assertEquals(data[1].get('pincode'), self.pincode)
        self.assertEquals(data[1].get('movie_name'), self.movie2.name)
        self.assertEquals(data[1].get('movie'), str(self.movie2.id))
        self.assertEquals(data[1].get('status'), "active")
