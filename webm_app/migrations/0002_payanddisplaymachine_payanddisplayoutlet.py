# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-21 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webm_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayAndDisplayMachine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(verbose_name='Latitude co-ordinate')),
                ('longitude', models.FloatField(verbose_name='Longitude co-ordinate')),
                ('tariff', models.FloatField(verbose_name='Price per hour')),
                ('hours', models.TextField(verbose_name='The hours of operation')),
                ('zone', models.TextField(verbose_name='What zone the P&D machine is in')),
                ('location', models.TextField(verbose_name='Text location')),
                ('furtherloc', models.TextField(verbose_name='Further description of location')),
                ('nospaces', models.TextField(verbose_name='Number of total parking spaces in street/area')),
                ('furtherinfo', models.TextField(verbose_name='Further information')),
                ('clearway', models.BinaryField(verbose_name='Machine is in a clearway zone')),
            ],
        ),
        migrations.CreateModel(
            name='PayAndDisplayOutlet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(verbose_name='Latitude co-ordinate')),
                ('longitude', models.FloatField(verbose_name='Longitude co-ordinate')),
                ('name', models.TextField(verbose_name='Name of outlet')),
                ('address1', models.TextField(verbose_name='First address field')),
                ('address2', models.TextField(verbose_name='Second address field')),
                ('county', models.TextField(verbose_name='County or Dublin area code')),
            ],
        ),
    ]
