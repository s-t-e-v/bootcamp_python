from datetime import datetime
from recipe import Recipe
import sys


class Book:

    def __init__(self, name):
        self.name = name
        self.creation_date = datetime.now()
        self.last_update = None
        self.recipes_list = {
            'starter': [],
            'lunch': [],
            'dessert': []
        }

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name and returns the instance"""
        for type, recipes in self.recipes_list.items():
            for recipe in recipes:
                if recipe.name == name:
                    print(recipe)
                    return recipe
        return None

    def get_recipes_by_types(self, recipe_type):
        """Gets all recipes names for a given recipe_type """
        recipes_list = self.recipes_list[recipe_type]
        if recipes_list:
            return [recipe.name for recipe in recipes_list]
        return []

    def add_recipe(self, recipe):
        """Adds a recipe to the book and updates last_update"""
        if not isinstance(recipe, Recipe):
            print("Error: recipe must be an instance of Recipe",
                  file=sys.stderr)
            return
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()
