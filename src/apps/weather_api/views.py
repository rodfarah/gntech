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
    """
    A view to retrieve a paginated list of temperature data.
    This view handles GET requests to display a list of all weather data entries,
    serialized using WeatherDataSerializer and paginated according to StandardPagination.
    Attributes:
        queryset: Retrieves all WeatherData objects from the database.
        serializer_class: Uses WeatherDataSerializer to convert model instances to JSON.
        pagination_class: Implements StandardPagination for the response.
    """

    queryset = models.WeatherData.objects.all()
    serializer_class = serializer.WeatherDataSerializer
    pagination_class = StandardPagination


@extend_schema(
    summary="Retrieve temperature records for a specific city",
    description="Returns all temperature records for the specified city",
    parameters=[
        OpenApiParameter(
            name="city_name",
            description="Name of the city to filter by",
            required=True,
            type=str,
            location=OpenApiParameter.PATH,
        ),
    ],
    responses={200: serializer.WeatherDataSerializer(many=True)},
    examples=[
        OpenApiExample(
            name="city_weather_data_example",
            summary="Example city weather data",
            description="Temperature records for a specific city",
            value={
                "count": 3,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "city": "São Paulo",
                        "temperature": 23.5,
                        "time": "2025-04-01T14:30:00Z",
                    },
                    {
                        "city": "São Paulo",
                        "temperature": 22.8,
                        "time": "2025-04-01T13:30:00Z",
                    },
                    {
                        "city": "São Paulo",
                        "temperature": 24.2,
                        "time": "2025-04-01T12:30:00Z",
                    },
                ],
            },
            response_only=True,
            status_codes=["200"],
        )
    ],
)
class TemperatureByCityDetailView(generics.ListAPIView):
    queryset = models.WeatherData.objects.all()
    serializer_class = serializer.WeatherDataSerializer

    def get_queryset(self):
        city_name = self.kwargs.get("city_name")
        queryset = models.WeatherData.objects.filter(city=city_name)
        return queryset
