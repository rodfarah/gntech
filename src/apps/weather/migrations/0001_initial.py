# Generated by Django 5.1.7 on 2025-04-01 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="WeatherData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("city", models.CharField(max_length=120)),
                ("temperature", models.FloatField()),
                ("time", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-time"],
            },
        ),
    ]
