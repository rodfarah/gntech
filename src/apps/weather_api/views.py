from drf_spectacular.utils import OpenApiExample, OpenApiParameter, extend_schema
from rest_framework import generics

from . import models, serializer
from .paginator import StandardPagination


@extend_schema(
    summary="Any user may retrieve a list all temperature records from Database",
    description="Returns a paginated list of all temperature records stored in the "
    "database",
    parameters=[
        OpenApiParameter(
            name="page",
            description="Page number for pagination",
            required=False,
            type=int,
        ),
        OpenApiParameter(
            name="page_size",
            description="Number of records per page (default as configured in "
            "StandardPagination)",
            required=False,
            type=int,
        ),
    ],
    responses={200: serializer.WeatherDataSerializer(many=True)},
    examples=[
        OpenApiExample(
            name="weather_data_example",
            summary="Example weather data",
            description="A paginated list of weather data records",
            value={
                "count": 25,
                "next": "http://example.com/api/temperatures/?page=2",
                "previous": None,
                "results": [
                    {
                        "city": "São Paulo",
                        "temperature": 23.5,
                        "time": "2025-04-01T14:30:00Z",
                    },
                    {
                        "city": "Rio de Janeiro",
                        "temperature": 28.2,
                        "time": "2025-04-01T14:30:00Z",
                    },
                    {
                        "city": "New York",
                        "temperature": 15.7,
                        "time": "2025-04-01T14:30:00Z",
                    },
                ],
            },
            response_only=True,
            status_codes=["200"],
        )
    ],
)
class TemperatureListView(generics.ListAPIView):
    queryset = models.WeatherData.objects.all()
    serializer_class = serializer.WeatherDataSerializer
    pagination_class = StandardPagination
