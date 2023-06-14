from book import Book
from recipe import Recipe

#All Errors for a recipe
# error = Recipe(1, "4", "1", {"1", "2", "3"}, 3, 6)
# to_print = str(error)
# print(to_print)
# print()

# error = Recipe("", 10, -74, [], "", "")
# to_print = str(error)
# print(to_print)
# print()

# error = Recipe("cake", 3, 15, ['eggs', 'flour', 3], "", "dessert")
# to_print = str(error)
# print(to_print)
# print()

#good recipe
cake_recipe = Recipe("cake", 2, 25, ['eggs', 'flour', 'milk'], "simple cake", "dessert")
to_print = str(cake_recipe)
print(to_print)
print()

# error = Book(3)
# error = Book("")
my_book = Book("Recipe Book")
omelette_recipe = Recipe("omelette", 1, 10, ['eggs', 'salt', 'pepper'], "simple omelette", "lunch")
croissant_recipe = Recipe("croissant", 4, 45, ['flour', 'water'], "", "lunch")
fries_recipe = Recipe("fries", 1, 10, ['potatoes', 'oil'], "", "starter")
fake_recipe = 3
my_book.add_recipe(omelette_recipe)
my_book.add_recipe(croissant_recipe)
my_book.add_recipe(fries_recipe)
my_book.add_recipe(fake_recipe)
my_book.add_recipe(cake_recipe)
print()
# new_recipe = my_book.get_recipe_by_name()
new_recipe = my_book.get_recipe_by_name("")
new_recipe = my_book.get_recipe_by_name("fake")
new_recipe = my_book.get_recipe_by_name("cake")
print()
# my_book.get_recipes_by_types()
my_book.get_recipes_by_types("")
my_book.get_recipes_by_types("fake")
print(my_book.get_recipes_by_types("lunch"))
print(my_book.get_recipes_by_types("dessert"))











