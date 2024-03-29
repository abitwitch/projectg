# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-06 00:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('grumblee', '0007_auto_20180703_0156'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryItem',
            fields=[
                ('guid', models.CharField(default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('overrideVal', models.IntegerField()),
                ('foodItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grumblee.FoodItem')),
            ],
        ),
        migrations.RemoveField(
            model_name='grocerylist',
            name='foodItems',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='minutesRequired',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='servings',
            field=models.PositiveIntegerField(),
        ),
        migrations.AddField(
            model_name='groceryitem',
            name='week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grumblee.GroceryList'),
        ),
    ]
