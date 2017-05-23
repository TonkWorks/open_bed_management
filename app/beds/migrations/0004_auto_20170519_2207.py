# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-20 02:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beds', '0003_auto_20170518_0249'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Status', 'verbose_name_plural': 'Statuses'},
        ),
        migrations.AddField(
            model_name='bed',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bed',
            name='room',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='bed',
            name='status',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='beds.Status'),
        ),
        migrations.AlterField(
            model_name='bed',
            name='tags',
            field=models.ManyToManyField(blank=True, to='beds.Tag'),
        ),
    ]