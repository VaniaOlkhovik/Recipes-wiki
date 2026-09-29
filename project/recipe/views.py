from django.shortcuts import render

# Create your views here.

from .models import Recipe
from .forms import RecipeForm
from django.views.generic import *
from django.urls import reverse_lazy

class HomeView(TemplateView):
    template_name = 'recipe/home.html'

class RecipesListView(ListView):
    model = Recipe
    template_name = 'recipe/recipes_list.html'
    context_object_name = 'recipes'

class CreateRecipeView(CreateView):
    template_name = 'recipe/create_recipe.html'
    form_class = RecipeForm
    success_url = reverse_lazy("recipe_list")

class RecipeDetailView(DetailView):
    template_name = "recipe/recipe_detail.html"
    model = Recipe
    context_object_name = 'recipe'

class RecipeUpdateView(UpdateView):
    template_name = 'recipe/update_recipe.html'
    model = Recipe
    form_class = RecipeForm  
    success_url = reverse_lazy("recipe_list")
    
class RecipeDeleteView(DeleteView):
    success_url = reverse_lazy("recipe_list")
    model = Recipe