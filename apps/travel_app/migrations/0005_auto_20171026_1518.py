# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-26 22:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0004_auto_20171026_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='travel_date_from',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trip',
            name='travel_date_to',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
