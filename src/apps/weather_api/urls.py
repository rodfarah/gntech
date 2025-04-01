from django.urls import path

from . import views

app_name = "weather_api"

urlpatterns = [
    # TEMPERATURE API PATHS
    # List of all temperature objects available in DB
    path("temperatures/", views.TemperatureListView.as_view(), name="temperature_list")
]
