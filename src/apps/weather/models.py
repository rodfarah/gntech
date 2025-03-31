from django.db import models


class WeatherData(models.Model):
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    country = models.CharField(max_length=100)
    temperature = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-time"]