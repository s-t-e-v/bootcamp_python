import sys


class Recipe:
    recipe_types = ["starter", "lunch", "dessert"]

    def __init__(
            self,
            name,
            cooking_lvl,
            cooking_time,
            ingredients,
            recipe_type,
            description=""
            ):
        if not isinstance(name, str):
            print("Error: name must be a string", file=sys.stderr)
            sys.exit(1)
        self.name = name
        if not isinstance(cooking_lvl, int):
            print("Error: cooking_lvl must be an integer",
                  file=sys.stderr)
            sys.exit(1)
        if not 1 <= cooking_lvl <= 5:
            print("Error: cooking_lvl must be between 1 and 5",
                  file=sys.stderr)
            sys.exit(1)
        self.cooking_lvl = cooking_lvl
        if not isinstance(cooking_time, int):
            print("Error: cooking_time must be an integer",
                  file=sys.stderr)
            sys.exit(1)
        if cooking_time < 0:
            print("Error: cooking_time must be non-negative",
                  file=sys.stderr)
            sys.exit(1)
        self.cooking_time = cooking_time
        if not isinstance(ingredients, list):
            print("Error: ingredients must be a list",
                  file=sys.stderr)
            sys.exit(1)
        if not all(isinstance(s, str) for s in ingredients):
            print("Error: all ingredients must be strings",
                  file=sys.stderr)
            sys.exit(1)
        self.ingredients = ingredients
        if not isinstance(recipe_type, str):
            print("Error: recipe_type must be a string",
                  file=sys.stderr)
            sys.exit(1)
        if recipe_type not in self.recipe_types:
            print(f"Error: recipe_type must be one of {self.recipe_types}",
                  file=sys.stderr)
            sys.exit(1)
        self.recipe_type = recipe_type
        if not isinstance(description, str):
            print("Error: description must be a string",
                  file=sys.stderr)
            sys.exit(1)
        self.description = description

    def __str__(self):
        """Returns the string to print with the recipe's info"""
        txt = (
            f"{{name: '{self.name}', "
            f"cooking_lvl: {self.cooking_lvl}, "
            f"cooking_time: {self.cooking_time}, "
            f"'ingredients': {self.ingredients}, "
            f"description: '{self.description}', "
            f"recipe_type: '{self.recipe_type}'}}"
        )
        return txt
