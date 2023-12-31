# Generated by Django 5.0 on 2024-01-08 12:47

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.TextField()),
                ('model', models.CharField(max_length=50)),
                ('mark', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cars.category')),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(default=datetime.datetime(2024, 2, 7, 12, 47, 21, 580179, tzinfo=datetime.timezone.utc))),
                ('cost', models.FloatField(default=0.0)),
                ('is_active', models.BooleanField(default=True)),
                ('car', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
            ],
        ),
    ]
