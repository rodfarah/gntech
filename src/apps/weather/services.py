"""
Services to consume OpenWeather API data
Please, notice that OpenWeather demands city geo coordinates and not city names. So
we have to obtain the city geo coordinates first and then we may get weather data.
"""

import requests
from django.conf import settings


class WeatherService:
    def __init__(self) -> None:
        self.api_key = settings.API_KEY
        # to obtain geo coordinates for a specific city, using GeocodingAPI
        self.url_coordinates_base_structure = (
            "http://api.openweathermap.org/geo/1.0/direct"
        )
        # to obtain weather information for specific geo coordinates, using OpenWeather
        self.url_weather_base_stucture = (
            "https://api.openweathermap.org/data/2.5/weather"
        )

    def get_city_geo_coordinates(self, city):
        """
        OpenWeather uses Geocoding API in order to obtain geo coordinates for a specific
        city.
        Please, check for further details:
        https://openweathermap.org/api/geocoding-api
        """
        params = {"city name": city, "appid": self.api_key, "limit": 1}

        response = requests.get(url=self.url_coordinates_base_structure, params=params)

        return response.json()
