# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from django.http import JsonResponse

from .models import Recipe
from .models import Week
from .models import Day
from .models import Ingredient
from .models import GroceryItem
from .models import RecipeIngredients

import json



def index(request):

    return render(request, 'index.html')
    #return HttpResponse('plan. eat. share.')

def reacttest(request):

    return render(request, 'reacttest.html')
    #return HttpResponse('plan. eat. share.')

def plan(request):
    recipes = Recipe.objects.all()[:10]
    ingredients = Ingredient.objects.all()[:10]
    week = Week.objects.create()
    context = {
        'recipes': recipes,
        'week': week,
        'ingredients': ingredients,
        'test':'te"st',
        'days': str(json.dumps(getDaysOfWeekAsJson(week.guid)))
    }
    return render(request, 'plan.html', context)

def addRecipeToDay(request):
    recipeGuid=request.GET.get('recipeGuid', None)
    dayGuid=request.GET.get('dayGuid', None)
    day=Day.objects.get(guid=dayGuid)
    weekGuid=day.week.guid
    recipe=Recipe.objects.get(guid=recipeGuid)
    day.recipes.add(recipe)
    ingredients={}
    for recipeIngredient in RecipeIngredients.objects.filter(recipe=recipe):
        ingredients[recipeIngredient.ingredient.guid]=recipeIngredient.quantity
        updateIngredientForWeek_fn(recipeIngredient.ingredient.guid,weekGuid,recipeIngredient.quantity)
    day.save()
    context = {
        'status':'success',
        'ingredients':ingredients
    }
    return JsonResponse(context)

def removeRecipeFromDay(request):
    recipeGuid=request.GET.get('recipeGuid', None)
    dayGuid=request.GET.get('dayGuid', None)
    day=Day.objects.get(guid=dayGuid)
    weekGuid=day.week.guid
    recipe=Recipe.objects.get(guid=recipeGuid)
    day.recipes.remove(Recipe.objects.get(guid=recipeGuid))
    ingredients={}
    for recipeIngredient in RecipeIngredients.objects.filter(recipe=recipe):
        ingredients[recipeIngredient.ingredient.guid]=(-1)*recipeIngredient.quantity
        updateIngredientForWeek_fn(recipeIngredient.ingredient.guid,weekGuid,(-1)*recipeIngredient.quantity)
    day.save()
    context = {
        'status':'success',
        'ingredients':ingredients
    }
    return JsonResponse(context)

def updateIngredientForWeek(request):
    ingredientGuid=request.GET.get('ingredientGuid', None)
    weekGuid=request.GET.get('weekGuid', None)
    overrideVal=int(request.GET.get('overrideVal', None))
    context={}
    if(updateIngredientForWeek_fn(ingredientGuid,weekGuid,overrideVal)):
        context['status']='success'
    else:
        context['status']='failure'
    return JsonResponse(context)

def updateIngredientForWeek_fn(ingredientGuid,weekGuid,overrideVal):
    ingredient=Ingredient.objects.get(guid=ingredientGuid)
    week=Week.objects.get(guid=weekGuid)
    groceryItem = GroceryItem.objects.get_or_create(week=week,ingredient=ingredient)[0]
    groceryItem.overrideVal+=overrideVal
    groceryItem.save()
    return True

def getDaysOfWeekAsJson(weekGuid):
    week=Week.objects.get(guid=weekGuid)
    context = [
        {'id': week.day1.guid, 'dayName': week.day1.date.strftime("%A"), 'date': week.day1.date.strftime("%Y-%m-%d")},
        {'id': week.day2.guid, 'dayName': week.day2.date.strftime("%A"), 'date': week.day2.date.strftime("%Y-%m-%d")},
        {'id': week.day3.guid, 'dayName': week.day3.date.strftime("%A"), 'date': week.day3.date.strftime("%Y-%m-%d")},
        {'id': week.day4.guid, 'dayName': week.day4.date.strftime("%A"), 'date': week.day4.date.strftime("%Y-%m-%d")},
        {'id': week.day5.guid, 'dayName': week.day5.date.strftime("%A"), 'date': week.day5.date.strftime("%Y-%m-%d")},
        {'id': week.day6.guid, 'dayName': week.day6.date.strftime("%A"), 'date': week.day6.date.strftime("%Y-%m-%d")},
        {'id': week.day7.guid, 'dayName': week.day7.date.strftime("%A"), 'date': week.day7.date.strftime("%Y-%m-%d")}
    ]
    return context
