# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-20 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beds', '0004_auto_20170519_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='icon',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='status',
            name='style',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='tag',
            name='icon',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='tag',
            name='style',
            field=models.CharField(default='', max_length=255),
        ),
    ]
