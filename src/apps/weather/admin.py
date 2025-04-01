from django.contrib import admin

from .models import WeatherData

# change Django Administrator (title)
admin.site.site_header = "gntech - OpenWeather API Panel"


@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = ("city", "temperature", "time")
    search_fields = ["city"]
    list_filter = ["time"]
