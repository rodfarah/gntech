"""
Only ADMIN person may retrieve data from OpenWeather API using the API endpoints
bellow.
"""

from django.urls import path

from . import views

app_name = "weather"

urlpatterns = [
    # The following path will retrieve weather data for a specific city,
    # from OpenWeather API
    path(
        "get-temperature/<str:city>",
        views.GetTemperatureByCity.as_view(),
        name="get_current_temperature_by_city",
    )
]
