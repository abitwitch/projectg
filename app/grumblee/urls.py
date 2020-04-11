from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^plan/', views.plan, name='plan'),
    url(r'^view/(?P<weekGuid>.+)/$', views.view, name='view'),
    url(r'^shop/(?P<weekGuid>.+)/$', views.shop, name='shop'),
    url(r'^reacttest/', views.reacttest, name='reacttest'),
    url(r'^addRecipeToDay/', views.addRecipeToDay, name='addRecipeToDay'),
    url(r'^removeRecipeFromDay/', views.removeRecipeFromDay, name='removeRecipeFromDay'),
    url(r'^updateIngredientForWeek/', views.updateIngredientForWeek, name='updateIngredientForWeek'),
]
