from django.contrib import admin
from .models import Recipe, RecipeIngredient, Profile


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]