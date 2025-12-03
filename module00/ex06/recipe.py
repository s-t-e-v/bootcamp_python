# Part 1: Nested Dictionaries
sandwich = {
    'ingredients': ["ham", "bread", "cheese", "tomatoes"],
    'meal': "lunch",
    'prep_time': 10
}
cake = {
    'ingredients': ["flour", "sugar", "eggs"],
    'meal': "dessert",
    'prep_time': 60
}
salad = {
    'ingredients': ["avocado", "arugula", "tomatoes", "spinach"],
    'meal': "lunch",
    'prep_time': 15
}

cookbook = {
    'Sandwich': sandwich,
    'Cake': cake,
    'Salad': salad
}


# Part 2: A Handful of Helpful Functions
def print_all_recipe_names():
    print(f"{'\n'.join(k for k, v in cookbook.items())}")


def recipe_details(recipe_name):
    recipe = cookbook.get(recipe_name)
    if not recipe:
        return
    print(f"""\
Recipe for {recipe_name}:
    Ingredients list: {", ".join(v for v in recipe['ingredients'])}
    To be eaten for {recipe['meal']}.
    Takes {recipe['prep_time']} minutes of cooking.""")


def delete_recipe_by_name(recipe_name):
    if (recipe_name in cookbook):
        del cookbook[recipe_name]


def add_recipe():
    print("Enter a name:")
    recipe_name = input()
    print("Enter ingredients:")
    ingredient_list = []
    while True:
        ingredient = input()
        if not ingredient:
            break
        ingredient_list.append(ingredient)
    print("Enter a meal type:")
    meal = input()
    print("Enter a preparation time:")
    prep_time = input()
    cookbook[recipe_name] = {
        'ingredients': ingredient_list,
        'meal': meal,
        'prep_time': prep_time
    }


# Part 3: A command line executable !
def delete_recipe():
    print("Please enter the recipe name to delete:")
    recipe_name = input()
    delete_recipe_by_name(recipe_name)


def print_recipe():
    print("Please enter a recipe name to get its details:")
    recipe_name = input()
    recipe_details(recipe_name)


def print_cookbook():
    for recipe_name in cookbook:
        recipe_details(recipe_name)
        print("")


print("Welcome to the Python Cookbook !")
while True:
    print("""
List of available options:
    1: Add a recipe
    2: Delete a recipe
    3: Print a recipe
    4: Print the cookbook
    5: Quit

Please select an option:
    """)
    try:
        selected_option = int(input())
    except ValueError:
        print("Sorry, this option does not exist.")
        continue
    if not 1 <= selected_option <= 5:
        print("Sorry, this option does not exist.")
        continue
    match selected_option:
        case 1:
            add_recipe()
        case 2:
            delete_recipe()
        case 3:
            print_recipe()
        case 4:
            print_cookbook()
        case 5:
            print("Cookbook closed. Goodbye !")
            break
