# Generated by Django 3.2 on 2022-10-15 09:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Menu",
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
                ("title", models.CharField(max_length=100)),
                ("category", models.IntegerField(default=0)),
                ("description", models.TextField(blank=True)),
                ("menu_image", models.TextField(blank=True)),
                ("price", models.FloatField(default=0)),
                ("status", models.IntegerField(default=1)),
                ("date_added", models.DateTimeField(default=django.utils.timezone.now)),
                ("date_updated", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]