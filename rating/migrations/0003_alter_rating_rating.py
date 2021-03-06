# Generated by Django 3.2.13 on 2022-05-06 17:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rating", "0002_onscreen_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rating",
            name="rating",
            field=models.PositiveSmallIntegerField(
                validators=[
                    django.core.validators.MaxValueValidator(10),
                    django.core.validators.MinValueValidator(1),
                ]
            ),
        ),
    ]
