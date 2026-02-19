from django.shortcuts import render

recipes_list_context = {
    'recipes': [
        {
            'name': 'Recipe 1',
            'ingredients': [
                {'name': 'tomato', 'quantity': '3pcs'},
                {'name': 'onion', 'quantity': '1pc'},
                {'name': 'pork', 'quantity': '1kg'},
                {'name': 'water', 'quantity': '1L'},
                {'name': 'sinigang mix', 'quantity': '1 packet'},
            ],
            'link': '/recipe/1',
        },
        {
            'name': 'Recipe 2',
            'ingredients': [
                {'name': 'garlic', 'quantity': '1 head'},
                {'name': 'onion', 'quantity': '1pc'},
                {'name': 'vinegar', 'quantity': '1/2 cup'},
                {'name': 'water', 'quantity': '1 cup'},
                {'name': 'salt', 'quantity': '1 tablespoon'},
                {'name': 'whole black peppers', 'quantity': '1 tablespoon'},
                {'name': 'pork', 'quantity': '1 kilo'},
            ],
            'link': '/recipe/2',
        },
    ]
}

recipe_1_context = {
    'name': 'Recipe 1',
    'ingredients': [
        {'name': 'tomato', 'quantity': '3pcs'},
        {'name': 'onion', 'quantity': '1pc'},
        {'name': 'pork', 'quantity': '1kg'},
        {'name': 'water', 'quantity': '1L'},
        {'name': 'sinigang mix', 'quantity': '1 packet'},
    ],
}

recipe_2_context = {
    'name': 'Recipe 2',
    'ingredients': [
        {'name': 'garlic', 'quantity': '1 head'},
        {'name': 'onion', 'quantity': '1pc'},
        {'name': 'vinegar', 'quantity': '1/2 cup'},
        {'name': 'water', 'quantity': '1 cup'},
        {'name': 'salt', 'quantity': '1 tablespoon'},
        {'name': 'whole black peppers', 'quantity': '1 tablespoon'},
        {'name': 'pork', 'quantity': '1 kilo'},
    ],
}

def recipes_list(request):
    return render(request, 'recipe_list.html', recipes_list_context)

def recipe_1(request):
    return render(request, 'recipe.html', recipe_1_context)

def recipe_2(request):
    return render(request, 'recipe.html', recipe_2_context)