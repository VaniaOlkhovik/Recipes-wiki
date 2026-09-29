from django.urls import path
from .views import HomeView, RecipesListView, CreateRecipeView, RecipeDetailView, RecipeUpdateView, RecipeDeleteView

urlpatterns = [
    path("home/", HomeView.as_view(), name = "home"),
    path("recipe/all/", RecipesListView.as_view(), name = "recipe_list"),
    path("recipe/create/", CreateRecipeView.as_view(), name = "create_recipe"),
    path("recipe/detail/<int:pk>", RecipeDetailView.as_view(), name = "detail_recipe"),
    path("recipe/delete/<int:pk>", RecipeDeleteView.as_view(), name = "delete_recipe"),
    path("recipe/update/<int:pk>", RecipeUpdateView.as_view(), name = "update_recipe")
]
