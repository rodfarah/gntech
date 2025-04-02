"""
Only ADMIN person may retrieve data from OpenWeather API using the API endpoints
bellow.
"""

from django.urls import path

from . import views

app_name = "weather"

urlpatterns = [
    # TEMPERATURE API PATHS
    # List of all temperature objects available in DB
    path(
        "get-temperature/<str:city>",
        views.GetTemperatureByCity.as_view(),
        name="get_current_temperature_by_city",
    )
]
