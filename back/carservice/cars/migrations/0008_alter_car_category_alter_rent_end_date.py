# Generated by Django 5.0 on 2024-02-15 06:02

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_alter_car_picture_alter_rent_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.category'),
        ),
        migrations.AlterField(
            model_name='rent',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 16, 6, 2, 28, 966174, tzinfo=datetime.timezone.utc)),
        ),
    ]