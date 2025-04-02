"""
Any user may retrieve data from database using this API endpoints
"""

from django.urls import path

from . import views

app_name = "weather_api"

urlpatterns = [
    # Lists all wheather data objects available in DB, for all requested cities.
    path(
        "temperatures/all-records/",
        views.TemperatureListView.as_view(),
        name="all_temperature_list",
    ),
    # Lists all weather data objects available in DB, for a specific city.
    path(
        "temperatures/by-city/<str:city_name>/",
        views.TemperatureByCityDetailView.as_view(),
        name="temperature_by_city",
    ),
]
