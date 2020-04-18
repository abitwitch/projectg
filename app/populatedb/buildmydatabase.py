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
    name,minutesRequired,servings,steps,ingredientsWithquantities=line.split("|")
    r = Recipe(name='',steps='',minutesRequired=45,servings=4)
    for ingredientWithquantities in ingredientsWithquantities:
        ingredientWithquantities

'''
r = Recipe(name='',steps='',minutesRequired=45,servings=4)
r.save()

i = Ingredient(name='')
i.save()

ri = RecipeIngredients(recipe=r,ingredient=i,quantity=5)
ri.save()
'''
