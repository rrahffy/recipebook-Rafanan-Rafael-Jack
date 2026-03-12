from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Recipe, RecipeImage
from .forms import RecipeForm, RecipeImageForm


def recipes_list(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'recipe_list.html', context)


@login_required
def recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    context = {'recipe': recipe}
    return render(request, 'recipe.html', context)


@method_decorator(login_required, name='dispatch')
class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_add.html'
    success_url = reverse_lazy('recipes_list')


@method_decorator(login_required, name='dispatch')
class RecipeImageCreateView(CreateView):
    model = RecipeImage
    form_class = RecipeImageForm
    template_name = 'recipe_add_image.html'

    def form_valid(self, form):
        form.instance.recipe = get_object_or_404(Recipe, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('recipe', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = get_object_or_404(Recipe, pk=self.kwargs['pk'])
        return context