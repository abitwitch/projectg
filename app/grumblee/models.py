# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime, timedelta
import uuid

from django.db import models

'''
class User(models.Model):
    firstName=models.CharField(max_length=200)
    lastName=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    loginname=models.CharField(max_length=200, default=email)
    password=models.CharField(max_length=200)
    created_at=models.DateTimeField(default=datatime.now, blank=true)
'''


class Ingredient(models.Model):
    guid=models.CharField(primary_key=True, max_length=100, blank=False, unique=True, default=uuid.uuid4)
    name=models.CharField(max_length=100)
    isStaple=models.BooleanField(default=False)
    defaultQuantity=models.PositiveIntegerField(default=1)
    pluCode=models.CharField(max_length=10, blank=True, null=True)
    def __str__(self):
        return str(self.name)

class Recipe(models.Model):
    guid=models.CharField(primary_key=True, max_length=100, blank=False, unique=True, default=uuid.uuid4)
    name=models.CharField(max_length=100)
    steps=models.TextField()
    minutesRequired=models.PositiveIntegerField()
    servings=models.PositiveIntegerField()
    def __str__(self):
        return str(self.name)

class RecipeIngredients(models.Model):
    guid=models.CharField(primary_key=True, max_length=100, blank=False, unique=True, default=uuid.uuid4)
    recipe=models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient=models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    def __str__(self):
        return str(self.guid)

class Day(models.Model):
    guid=models.CharField(primary_key=True, max_length=100, blank=False, unique=True, default=uuid.uuid4)
    recipes=models.ManyToManyField(Recipe, blank=True)
    week=models.ForeignKey('Week', on_delete=models.CASCADE, blank=True, null=True)
    date=models.DateField()
    def __str__(self):
        return str(self.guid)

class Week(models.Model):
    guid=models.CharField(primary_key=True, max_length=100, blank=False, unique=True, default=uuid.uuid4)
    #user=models.ForeignKey(USER, on_delete=models.CASCADE)
    day1=models.ForeignKey(Day, on_delete=models.CASCADE, related_name='day1', blank=True, null=True)
    day2=models.ForeignKey(Day, on_delete=models.CASCADE, related_name='day2', blank=True, null=True)
    day3=models.ForeignKey(Day, on_delete=models.CASCADE, related_name='day3', blank=True, null=True)
    day4=models.ForeignKey(Day, on_delete=models.CASCADE, related_name='day4', blank=True, null=True)
    day5=models.ForeignKey(Day, on_delete=models.CASCADE, related_name='day5', blank=True, null=True)
    day6=models.ForeignKey(Day, on_delete=models.CASCADE, related_name='day6', blank=True, null=True)
    day7=models.ForeignKey(Day, on_delete=models.CASCADE, related_name='day7', blank=True, null=True)
    def save(self, **kwargs):
        #Create the days if not set
        day1=datetime.today()
        if not self.day1:
            self.day1 = Day.objects.create(date=day1 + timedelta(days=0),guid=uuid.uuid4())
        if not self.day2:
            self.day2 = Day.objects.create(date=day1 + timedelta(days=1),guid=uuid.uuid4())
        if not self.day3:
            self.day3 = Day.objects.create(date=day1 + timedelta(days=2),guid=uuid.uuid4())
        if not self.day4:
            self.day4 = Day.objects.create(date=day1 + timedelta(days=3),guid=uuid.uuid4())
        if not self.day5:
            self.day5 = Day.objects.create(date=day1 + timedelta(days=4),guid=uuid.uuid4())
        if not self.day6:
            self.day6 = Day.objects.create(date=day1 + timedelta(days=5),guid=uuid.uuid4())
        if not self.day7:
            self.day7 = Day.objects.create(date=day1 + timedelta(days=6),guid=uuid.uuid4())
        #add the week to each day
        self.day1.week=self
        self.day2.week=self
        self.day3.week=self
        self.day4.week=self
        self.day5.week=self
        self.day6.week=self
        self.day7.week=self
        #Save the week
        super(Week, self).save(**kwargs)
        #Save the days
        self.day1.save()
        self.day2.save()
        self.day3.save()
        self.day4.save()
        self.day5.save()
        self.day6.save()
        self.day7.save()
    def __str__(self):
        return str(self.guid)

class GroceryList(models.Model):
    guid=models.CharField(primary_key=True, max_length=100, blank=False, unique=True, default=uuid.uuid4)
    week=models.ForeignKey(Week, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.guid)

class GroceryItem(models.Model):
    guid=models.CharField(primary_key=True, max_length=100, blank=False, unique=True, default=uuid.uuid4)
    week=models.ForeignKey(Week, on_delete=models.CASCADE)
    ingredient=models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    overrideVal=models.IntegerField(default=0)
    def __str__(self):
        return str(self.guid)

class RecipeList(models.Model):
    guid=models.CharField(primary_key=True, max_length=100, blank=False, unique=True, default=uuid.uuid4)
    #user=models.ForeignKey(USER, on_delete=models.CASCADE)
    recipes=models.ManyToManyField(Recipe)
    def __str__(self):
        return str(self.guid)
