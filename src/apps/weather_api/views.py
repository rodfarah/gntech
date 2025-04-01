from rest_framework import generics

from . import models, serializer
from .paginator import StandardPagination


class TemperatureListView(generics.ListAPIView):
    queryset = models.WeatherData.objects.all()
    serializer_class = serializer.WeatherDataSerializer
    pagination_class = StandardPagination
