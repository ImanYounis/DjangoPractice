# Generated by Django 5.0.7 on 2024-07-18 09:32

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Member",
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
                ("fname", models.CharField(max_length=100)),
                ("lname", models.CharField(max_length=255)),
                ("phone", models.IntegerField(null=True)),
                ("dob", models.DateField(null=True)),
            ],
        ),
    ]