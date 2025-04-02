"""
Services to consume OpenWeather API data
Please, notice that OpenWeather demands city geo coordinates and not city names. It
is mandatory to obtain the city geo coordinates first and then we may get weather data.
"""

from datetime import datetime

import requests
from django.conf import settings

from .models import WeatherData


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

        Args:
        city (str): Name of the city written in English.

        Returns:
        tuple: A tuple containing (latitude, longitude) as float values.

        Please, check for further details:
        https://openweathermap.org/api/geocoding-api
        """
        params = {"q": city, "appid": self.api_key, "limit": 1}

        response = requests.get(url=self.url_coordinates_base_structure, params=params)

        # raises exception if applicable
        response.raise_for_status()

        data = response.json()

        if not data:
            raise ValueError(
                "There is no data for this specific city. Are you sure "
                "you wrote the correct city name?"
            )

        latitude = data[0]["lat"]
        longitude = data[0]["lon"]

        return latitude, longitude

    def get_current_temperature(self, city):
        """
        Retrieves the current temperature for a specified city.
        The method first obtains geographical coordinates for the city, then makes a
        request to the OpenWeatherMap API to get current weather data. The temperature
        is returned in Celsius.
        Args:
            city (str): The name of the city to get the temperature for.
        Returns:
            float: The current temperature in Celsius.
        Raises:
            HTTPError: If the API request fails.
        """

        current_time = datetime.now()

        # obtain coordinates for city
        lat_and_lon = self.get_city_geo_coordinates(city)

        params = {
            "lat": lat_and_lon[0],
            "lon": lat_and_lon[1],
            "appid": self.api_key,
            "units": "metric",  # Celsius
            "lang": "pt_br",
        }

        response = requests.get(url=self.url_weather_base_stucture, params=params)

        # raises exception if applicable
        response.raise_for_status()

        data = response.json()
        current_temperature = data["main"]["temp"]

        # insert object inside PostgreSQL DB
        WeatherData.objects.create(
            city=city, temperature=current_temperature, time=current_time
        )

        return current_temperature
