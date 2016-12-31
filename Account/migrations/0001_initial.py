# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-31 04:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndexTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0, unique=True)),
                ('own_room_num', models.IntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='Interviewee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('telephone', models.CharField(default='', max_length=20)),
                ('addr', models.CharField(default='', max_length=200)),
                ('state', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='indextable',
            name='interviewee_list',
            field=models.ManyToManyField(to='Account.Interviewee'),
        ),
    ]
