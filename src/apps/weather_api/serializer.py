from rest_framework import serializers

from . import models


class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WeatherData
        fields = ["city", "temperature", "time"]
