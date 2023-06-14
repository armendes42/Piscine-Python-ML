import sys

class Recipe:

    def check_values(self, name, lvl, time, ingredients, desc, recipe_type):
        valid = True
        if not isinstance(name, str):
            print("Name must be a string.")
            valid = False
        if isinstance(name, str) and len(name) == 0:
            print("Name is empty.")
            valid = False
        if not isinstance(lvl, int) or not 1 <= lvl <= 5:
            print("Cooking_lvl must be an integer from 1 to 5 (both included).")
            valid = False
        if not isinstance(time, int) or not time >= 0:
            print("Cooking_time must be a positive integer.")
            valid = False
        if not isinstance(ingredients, list):
            print("Ingredients is not a list.")
            valid = False
        if isinstance(ingredients, list) and len(ingredients) == 0:
            print("Ingredients is empty.")
            valid = False
        for ingredient in ingredients:
            if not isinstance(ingredient, str):
                print("All of the ingredients must be string.")
                valid = False
        if desc is not None and not isinstance(desc, str):
            print("Description must be a string.")
            valid = False
        recipe_type_list = ["starter", "lunch", "dessert"]
        if not isinstance(recipe_type, str):
            print("Recipe_type must be a string.")
            valid = False
        if isinstance(recipe_type, str) and len(recipe_type) == 0:
            print("Recipe_type is empty.")
            valid = False
        if recipe_type not in recipe_type_list:
            print("Recipe_type must be 'starter', 'lunch' or 'dessert'.")
            valid = False
        return valid


    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        if self.check_values(name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
            self.name = name
            self.cooking_lvl = cooking_lvl
            self.cooking_time = cooking_time
            self.ingredients = ingredients 
            self.description = description
            self.recipe_type = recipe_type
        else:
            sys.exit(1)

    
    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ""
        txt += "The recipe name is: " + self.name + ". It's a " + self.recipe_type + " recipe."
        txt += "\nIt's a recipe of level " + str(self.cooking_lvl) + " and it needs " + str(self.cooking_time) + " minutes to cook."
        ingredients = ", ".join(self.ingredients)
        txt += "\nThe list of ingredients for this recipe are: " + ingredients + "."
        if self.description:
            txt += "\n" + self.description + "."
        return txt
    
tourte = Recipe("omelette", 4, 10, ['eggs', 'salt', 'pepper'], "", 'lunch')
to_print = str(tourte)
print(to_print)