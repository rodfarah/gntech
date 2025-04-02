from datetime import datetime

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from apps.weather_api.models import WeatherData


class TestTemperatureByCityListView(TestCase):
    def setUp(self) -> None:
        """Setup data for each test method"""
        self.client = APIClient()

        # create some test data
        self.tokio_data = WeatherData.objects.create(
            city="Tokio", temperature="12.5", time=datetime.now()
        )
        self.madrid_data = [
            WeatherData.objects.create(
                city="Madrid", temperature="12.5", time=datetime.now()
            ),
            WeatherData.objects.create(
                city="Madrid", temperature="21.3", time=datetime.now()
            ),
        ]

    def test_get_queryset_filters_by_city_name(self):
        url = reverse("weather_api:temperature_by_city", kwargs={"city_name": "Tokio"})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        # verify pagination structure
        self.assertIn("count", response.data)
        self.assertIn("results", response.data)

        # # verify if there is only 1 result (only "Tokio")
        self.assertEqual(response.data["count"], 1)

        # verify if Tokio is really the only result
        self.assertEqual(response.data["results"][0]["city"], "Tokio")

        # verify if Tokio temperature is correct
        self.assertEqual(response.data["results"][0]["temperature"], 12.5)
