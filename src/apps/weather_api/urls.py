"""
Any user may retrieve data from this API endpoints
"""

from django.urls import path

from . import views

app_name = "weather_api"

urlpatterns = [
    # List of all temperature objects available in DB
    path(
        "temperatures/all-records/",
        views.TemperatureListView.as_view(),
        name="all_temperature_list",
    ),
    path(
        "temperatures/by-city/<str:city_name>/",
        views.TemperatureByCityDetailView.as_view(),
        name="temperature_by_city",
    ),
]
