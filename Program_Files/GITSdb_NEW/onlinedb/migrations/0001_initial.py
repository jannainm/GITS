# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-05 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='C:\\Users\\jannainm\\workspace\\GITSdb_NEWdefault.png', upload_to=b'')),
                ('record_id', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField(verbose_name='created date')),
                ('crew_id', models.IntegerField(default=0)),
                ('supervisor_name', models.CharField(max_length=100)),
                ('date_on_site', models.DateTimeField(verbose_name='incident date')),
                ('cleanup_scale', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1)),
                ('building_type', models.CharField(choices=[('I', 'Industrial'), ('C', 'Commercial'), ('R', 'Residential')], default='I', max_length=1)),
                ('property_address', models.CharField(default='', max_length=100)),
                ('nearest_cross_street', models.CharField(default='', max_length=100)),
                ('gps_coordinates', models.CharField(default='', max_length=100)),
                ('moniker', models.CharField(default='', max_length=100)),
                ('number_of_images', models.IntegerField(default=0)),
            ],
        ),
    ]
