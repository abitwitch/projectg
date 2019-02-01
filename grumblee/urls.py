from django.conf.urls import url

from . import views
#this is a test
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^plan/', views.plan, name='plan'),
    url(r'^reacttest/', views.reacttest, name='reacttest'),
    url(r'^addRecipeToDay/', views.addRecipeToDay, name='addRecipeToDay'),
    url(r'^removeRecipeFromDay/', views.removeRecipeFromDay, name='removeRecipeFromDay'),
    url(r'^updateIngredientForWeek/', views.updateIngredientForWeek, name='updateIngredientForWeek'),
]
