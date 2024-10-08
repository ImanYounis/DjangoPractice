# Generated by Django 5.0.7 on 2024-08-05 10:12

import django_enum_choices.choice_builders
import django_enum_choices.fields
import user.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0011_alter_emp_relation"),
    ]

    operations = [
        migrations.CreateModel(
            name="Patient",
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
                ("patient_name", models.CharField(max_length=255)),
                (
                    "relation",
                    django_enum_choices.fields.EnumChoiceField(
                        choice_builder=django_enum_choices.choice_builders.value_value,
                        choices=[
                            ("Self", "Self"),
                            ("Spouse", "Spouse"),
                            ("Parent", "Parent"),
                            ("Child", "Child"),
                        ],
                        default=user.models.RelationsEnum["SELF"],
                        enum_class=user.models.RelationsEnum,
                        max_length=6,
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="emp",
            name="relation",
        ),
    ]
