# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-29 02:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grumblee', '0003_auto_20180629_0217'),
    ]

    operations = [
        migrations.AddField(
            model_name='week',
            name='day2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='day2', to='grumblee.Day'),
        ),
        migrations.AddField(
            model_name='week',
            name='day3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='day3', to='grumblee.Day'),
        ),
        migrations.AddField(
            model_name='week',
            name='day4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='day4', to='grumblee.Day'),
        ),
        migrations.AddField(
            model_name='week',
            name='day5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='day5', to='grumblee.Day'),
        ),
        migrations.AddField(
            model_name='week',
            name='day6',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='day6', to='grumblee.Day'),
        ),
        migrations.AddField(
            model_name='week',
            name='day7',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='day7', to='grumblee.Day'),
        ),
    ]
