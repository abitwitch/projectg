# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-29 02:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grumblee', '0002_auto_20180621_0158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='week',
            name='day2',
        ),
        migrations.RemoveField(
            model_name='week',
            name='day3',
        ),
        migrations.RemoveField(
            model_name='week',
            name='day4',
        ),
        migrations.RemoveField(
            model_name='week',
            name='day5',
        ),
        migrations.RemoveField(
            model_name='week',
            name='day6',
        ),
        migrations.RemoveField(
            model_name='week',
            name='day7',
        ),
        migrations.AlterField(
            model_name='week',
            name='day1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='day1', to='grumblee.Day'),
        ),
    ]
