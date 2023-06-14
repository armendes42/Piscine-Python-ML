import sys
import datetime
from recipe import Recipe

class Book:

    def __init__(self, name):
        valid = True
        if not isinstance(name, str):
            print("Name must be a string.")
            valid = False
        if isinstance(name, str) and len(name) == 0:
            print("Name is empty.")
            valid = False
        if valid:
            self.name = name
            self.last_update = datetime.datetime.now()
            self.creation_date = datetime.datetime.now()
            self.recipes_list = {"starter": [],
                                 "lunch": [],
                                 "dessert": []}
        else:
            sys.exit(1)


    def get_recipe_by_name(self, name):
        """Prints a recipe with the name {name} and returns the instance"""
        if not isinstance(name, str):
            print("Name must be a string.")
            return
        if isinstance(name, str) and len(name) == 0:
            print("Name is empty.")
            return
        for key, obj_list in self.recipes_list.items():
            for obj in obj_list:
                if obj.name == name:
                    return obj
        print("Name is not a recipe.")
        return


    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if not isinstance(recipe_type, str):
            print("Recipe_type must be a string.")
            return
        if isinstance(recipe_type, str) and len(recipe_type) == 0:
            print("Recipe_type is empty.")
            return
        result = ""
        for key, obj_list in self.recipes_list.items():
            if key == recipe_type:
                result += ", ".join(obj.name for obj in obj_list)
        if result == "":
            print("Recipe_type is not a good recipe_type.")
            return
        return result
                    

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        self.last_update = datetime.datetime.now()
        if not isinstance(recipe, Recipe):
            print("recipe is not a Recipe.")
            return
        recipe_type_list = ["starter", "lunch", "dessert"]
        if recipe.recipe_type in recipe_type_list:
            self.recipes_list[recipe.recipe_type].append(recipe)


