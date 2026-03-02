from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recipe

def recipes_list(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'recipe_list.html', context)

@login_required
def recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    context = {'recipe': recipe}
    return render(request, 'recipe.html', context)