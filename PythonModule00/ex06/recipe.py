sandwich = {"ingredients": ["ham", "bread", "cheese", "tomatoes"],
            "meal": "lunch",
            "prep_time": 10}

cake = {"ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60}

salad = {"ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
         "meal": "lunch",
         "prep_time": 15}

cookbook = {"sandwich": sandwich,
            "cake": cake,
            "salad": salad}


def print_all_recipes_name():
    print("The recipes in the cookbook are:")
    for key in cookbook:
        print(key)
    print()


def print_details_of_recipe():
    recipe_name = input("Please enter a recipe name to get its details:\n")

    if recipe_name in cookbook:
        print()
        print("Recipe for " + recipe_name + ":")
        ingredients = ""
        for index, ingredient in enumerate(cookbook[recipe_name]["ingredients"]):
            ingredients += "'" + ingredient + "'"
            if index != len(cookbook[recipe_name]["ingredients"]) - 1:
                ingredients += ", "
        print("   Ingredients list: [" + ingredients + "]")
        print("   To be eaten for " + cookbook[recipe_name]["meal"] + ".")
        print("   Takes " + str(cookbook[recipe_name]["prep_time"]) + " minutes of cooking.\n")
    else:
        print("This recipe is not in the cookbook !")
        print()


def delete_a_recipe():
    recipe_name = input("Please enter a recipe name to delete:\n")
    del cookbook[recipe_name]
    print()


def add_a_recipe():
    recipe_name = input("Enter a name:\n")
    print()
    print("Enter ingredients:")
    recipe_ingredients = []
    while True:
        ingredient = input().strip()

        if not ingredient:
            break

        recipe_ingredients.append(ingredient)

    recipe_meal = input("Enter a meal type:\n")
    print()
    recipe_prep_time = input("Enter a preparation time:\n")
    recipe = {"ingredients": recipe_ingredients,
              "meal": recipe_meal,
              "prep_time": recipe_prep_time}
    cookbook[recipe_name] = recipe
    print()


print("Welcome to the Python Cookbook !")
print("List of available option:")
print("   1: Add a recipe")
print("   2: Delete a recipe")
print("   3: Print a recipe")
print("   4: Print the cookbook")
print("   5: Quit\n")

options = [1, 2, 3, 4, 5]

while True:
    user_input = input("Please select an option:\n")
    if not user_input.isdigit() or int(user_input) not in options:
        print()
        print("Sorry, this option does not exist.")
        print("List of available option:")
        print("   1: Add a recipe")
        print("   2: Delete a recipe")
        print("   3: Print a recipe")
        print("   4: Print the cookbook")
        print("   5: Quit\n")

    else:
        print()
        option = int(user_input)
        if option == 1:
            add_a_recipe()
        elif option == 2:
            delete_a_recipe()
        elif option == 3:
            print_details_of_recipe()
        elif option == 4:
            print_all_recipes_name()
        elif option == 5:
            print("Cookbook closed. Goodbye !")
            break
