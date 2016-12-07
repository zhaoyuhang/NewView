# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-07 01:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='outdate_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 7, 9, 45, 25, 375521)),
        ),
        migrations.AlterField(
            model_name='manager',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]