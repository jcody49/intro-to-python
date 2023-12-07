import pickle

# Function to display a recipe
def display_recipe(recipe):
    print('Recipe:', recipe['name'])
    print('Cooking time (min):', recipe['cooking_time'])
    print('Ingredients:')
    for ingredient in recipe['ingredients']:
        print(ingredient)
    print('Difficulty:', recipe['difficulty'])

# Function to search for an ingredient in the given data
def search_ingredient(data, ingredient_searched): 
    all_ingredients = data.get('all_ingredients', [])

    if not all_ingredients:
        print("No ingredients found.")
        return

    # Display all available ingredients with index
    print("Available Ingredients:")
    for index, ingredient in enumerate(all_ingredients, 1):
        print(f"{index}. {ingredient}")

    try:
        # Get user input for ingredient search
        user_input = input("Enter the number of the ingredient to search: ")
        ingredient_index = int(user_input)
        print(f"DEBUG: Ingredient index selected: {ingredient_index}")
        ingredient_searched = all_ingredients[ingredient_index - 1]
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid number.")
        return

    print(f"DEBUG: Ingredient searched: {ingredient_searched}")

    # Search for the selected ingredient in recipes
    matching_recipes = [recipe for recipe in data['recipes_list'] if ingredient_searched in recipe['ingredients']]
    
    if matching_recipes:
        print(f"\nRecipes containing {ingredient_searched}:")
        for recipe in matching_recipes:
            display_recipe(recipe)
    else:
        print(f"\nNo recipes found containing {ingredient_searched}.")
# Main code
filename = input("Enter the name of the file containing your recipe data: ")

try:
    with open(filename, 'rb') as file:
        data = pickle.load(file)
except FileNotFoundError:
    print(f"File {filename} not found.")
else:
    # Call the search_ingredient function with data and None as arguments
    search_ingredient(data, None)
