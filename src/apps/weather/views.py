from drf_spectacular.utils import OpenApiExample, OpenApiParameter, extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .services import WeatherService


class GetTemperatureByCity(APIView):
    """
    A Django REST framework APIView class for retrieving the current temperature for a
    specified city. This view handles GET requests to fetch the current temperature for
    a city using an external weather service, and stores the retrieved data in the
    database.
    Methods:
        get(request, city=None): Retrieves the current temperature for the specified
        city.
    Returns:
        Response: A JSON response containing a success message and the city name if
        successful, or an appropriate error message with the corresponding HTTP status
        code.
    Raises:
        ValueError: If the city name is not found on the OpenWeather API or if the API
        returns an empty value.
        Exception: If there is a connection error or any other unexpected error occurs.
    Status Codes:
        - 200 OK: Temperature successfully retrieved and stored.
        - 404 Not Found: The specified city was not found.
        - 500 Internal Server Error: An unexpected error occurred.
    """

    @extend_schema(
        summary="An admin may get current temperature for a specific city",
        parameters=[
            OpenApiParameter(
                name="city",
                description="City Name (in English)",
                required=True,
                type=str,
                location=OpenApiParameter.PATH,
            )
        ],
        responses={
            200: {
                "type": "object",
                "properties": {
                    "message": {"type": "string"},
                    "city": {"type": "string"},
                },
                "example": {
                    "message": "The retrieval of the city's temperature was successful",
                    "city": "São Paulo",
                },
            },
            404: {
                "type": "object",
                "properties": {"error": {"type": "string"}},
                "example": {"error": "City not found"},
            },
            500: {
                "type": "object",
                "properties": {"error": {"type": "string"}},
                "example": {"error": "An unexpected server error occurred"},
            },
        },
        description="Retrieves the current temperature for the specific city",
    )
    def get(self, request, city=None):
        try:
            weather_service = WeatherService()
            weather_service.get_current_temperature(city=city)

            return Response(
                {
                    "message": "The retrieval of the city's temperature at the exact "
                    "moment, as well as the insertion of the data into the database, "
                    "were successfully performed.",
                    "city": city,
                },
                status=status.HTTP_200_OK,
            )
        # if city name is not found on OpenWeather API or if OpenWeather API returns
        # empty value
        except ValueError as e:
            return Response(
                {
                    "error": str(e),
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        # if there is an conection error with OpenWeather API, for instance
        except Exception as e:
            return Response(
                {"error": f"An unexpected error ocurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
