# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-23 02:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beds', '0006_auto_20170520_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlertRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_rule', models.TextField(default='{}')),
            ],
        ),
    ]
