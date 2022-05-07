from django.test import TestCase
from rating.models import Movie, Rating, User
from django.urls import reverse
from rest_framework.test import APIClient
import json


class TestFetchPostOfficeDetails(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.pincode = 110001
        return super().setUp()

    def test_fetch_postoffice_details_by_pincode(self):
        response = self.client.get(
            reverse("getPostOffice", kwargs={"PINCODE": self.pincode})
        )
        self.assertEquals(response.status_code, 200)
        json_data = json.loads(response.content)[0]
        self.assertEquals(json_data.get("Status"), "Success")
        postOffices = json_data.get("PostOffice")
        for postoffice in postOffices:
            self.assertEquals(postoffice.get("Pincode"), str(self.pincode))
            self.assertEquals(postoffice.get("Country"), "India")
            self.assertEquals(postoffice.get("State"), "Delhi")
