# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-03 07:41
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
                ('record_id', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField(verbose_name='created date')),
                ('crew_id', models.IntegerField(default=0)),
                ('supervisor_name', models.CharField(max_length=100)),
                ('date_on_site', models.DateTimeField(verbose_name='incident date')),
                ('cleanup_scale', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1)),
            ],
        ),
    ]
