# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-18 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bed',
            name='name',
            field=models.CharField(default='Bed', max_length=255),
        ),
        migrations.AlterField(
            model_name='log',
            name='log',
            field=models.TextField(default='{}'),
        ),
    ]