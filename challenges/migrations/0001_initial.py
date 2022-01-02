# Generated by Django 3.2.9 on 2021-11-15 15:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies: list[tuple[str, str]] = []

    operations = [
        migrations.CreateModel(
            name="Challenge",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("key", models.CharField(max_length=50, unique=True)),
                ("prompt", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("redirect_action", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="ChallengeShortLink",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("short_link", models.CharField(max_length=20, unique=True)),
                (
                    "challenge",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="challenges.challenge"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ChallengeSecret",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("secret", models.CharField(max_length=200)),
                (
                    "challenge",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="challenges.challenge"),
                ),
            ],
        ),
    ]
