import sys
sys.path.insert(1, '..')
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projectg.settings")
django.setup()
from django.conf import settings
from grumblee import models
models.Recipe


recipe_csv="recipes.csv"

with open(recipe_csv,"r") as f:
    content=f.read()

for line in content.split("\n")[1:]:
    if line.strip()=="":
        continue
    name,minutesRequired,servings,steps,ingredientsWithquantities=line.split("|")
    recipe = models.Recipe(name=name,steps=steps,minutesRequired=minutesRequired,servings=servings)
    recipe.save()
    for ingredientWithquantities in ingredientsWithquantities.split(";"):
        quantity,iname=ingredientWithquantities.split(" ", 1)
        iname=iname.strip()
        quantity=int(float(quantity))
        if quantity==0:
            quantity+=1
        ingredientExists=False
        for ingredient in models.Ingredient.objects.filter(name=iname):
            ingredientExists=True
            break
        if not ingredientExists:
            ingredient = models.Ingredient(name=iname,defaultQuantity=quantity*4)
            ingredient.save()
        recipeIngredient = models.RecipeIngredients(recipe=recipe,ingredient=ingredient,quantity=quantity)
        recipeIngredient.save()

print("done")
