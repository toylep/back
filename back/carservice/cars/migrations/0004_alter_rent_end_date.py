# Generated by Django 5.0 on 2023-12-24 15:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_rent_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 23, 15, 26, 33, 39161, tzinfo=datetime.timezone.utc)),
        ),
    ]