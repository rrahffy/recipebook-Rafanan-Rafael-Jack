from django.shortcuts import render

def recipes_list(request):
    return render(request, 'recipe_list.html')

def recipe_1(request):
    return render(request, 'recipe_1.html')

def recipe_2(request):
    return render(request, 'recipe_2.html')