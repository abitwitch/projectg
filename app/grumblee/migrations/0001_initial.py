# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-21 01:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('guid', models.CharField(default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=15)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('guid', models.CharField(default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('isStaple', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='GroceryList',
            fields=[
                ('guid', models.CharField(default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('foodItems', models.ManyToManyField(to='grumblee.FoodItem')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('guid', models.CharField(default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('steps', models.TextField()),
                ('minutesRequired', models.IntegerField()),
                ('servings', models.IntegerField()),
                ('foodItems', models.ManyToManyField(to='grumblee.FoodItem')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeList',
            fields=[
                ('guid', models.CharField(default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('recipes', models.ManyToManyField(to='grumblee.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('guid', models.CharField(default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('day1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='day1', to='grumblee.Day')),
                ('day2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='day2', to='grumblee.Day')),
                ('day3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='day3', to='grumblee.Day')),
                ('day4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='day4', to='grumblee.Day')),
                ('day5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='day5', to='grumblee.Day')),
                ('day6', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='day6', to='grumblee.Day')),
                ('day7', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='day7', to='grumblee.Day')),
            ],
        ),
        migrations.AddField(
            model_name='grocerylist',
            name='week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grumblee.Week'),
        ),
        migrations.AddField(
            model_name='day',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grumblee.Recipe'),
        ),
    ]
