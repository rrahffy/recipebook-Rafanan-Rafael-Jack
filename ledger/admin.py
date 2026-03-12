from django.contrib import admin
from .models import Recipe, RecipeIngredient, Profile, RecipeImage


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeImageInline(admin.TabularInline):
    model = RecipeImage


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline, RecipeImageInline]