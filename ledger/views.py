from django.shortcuts import render
from .models import Recipe

def recipes_list(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'recipe_list.html', context)

def recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    context = {'recipe': recipe}
    return render(request, 'recipe.html', context)