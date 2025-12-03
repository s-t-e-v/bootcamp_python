from recipe import Recipe
from book import Book


def display_book_content(book):
    print(f"My recipe book content:")
    for category in my_book.recipes_list:
        print(f"    '{category}':")
        for recipe in my_book.recipes_list[category]:
            print(f"         - {recipe}")


tourte = Recipe(
    "tourte",
    2,
    0,
    ["2", "1"],
    "starter"
)

print(tourte)

my_book = Book("Recettes de chez moi")
print(f"My recipe book name: {my_book.name}")
print("My recipe book creation date:", my_book.creation_date)
print(f"My recipe book last update: {my_book.last_update}")
print(f"My recipe book content: {my_book.recipes_list}")

my_book.add_recipe("2")
print("+new recipe")
my_book.add_recipe(tourte)
display_book_content(my_book)
print(f"--- My recipe book last update: {my_book.last_update} ---")
print("+new recipe")
my_book.add_recipe(Recipe(
    "Sandwich",
    1,
    0,
    ["bread", "ham", "cheese", "tomato"],
    "lunch"
))
print(f"--- My recipe book last update: {my_book.last_update} ---")
print("+new recipe")
my_book.add_recipe(Recipe(
    "Chocolate Cake",
    3,
    60,
    ["flour", "sugar", "cocoa powder", "eggs", "butter"],
    "dessert"
))
print(f"--- My recipe book last update: {my_book.last_update} ---")
print("+new recipe")
my_book.add_recipe(Recipe(
    "French Tacos",
    1,
    10,
    ["tortilla", "chicken", "fries", "cheese sauce"],
    "lunch",
    "A delicious French-style tacos."
))
display_book_content(my_book)
print(f"--- My recipe book last update: {my_book.last_update} ---")
print("Chocolate Cake details:")
chocolate_cake = my_book.get_recipe_by_name("Chocolate Cake")
print("Printing chocoalate cake object returned:")
print(chocolate_cake)
print("All lunch recipes:")
for recipe in my_book.get_recipes_by_types("lunch"):
    print(recipe)
