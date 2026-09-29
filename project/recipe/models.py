from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='recipes/')
    recipe = models.TextField()
    category = models.CharField(max_length=100, choices = [("desert", "Desert"), ("main_dish", "Main Food")])

def __str__(self):
    return self.name