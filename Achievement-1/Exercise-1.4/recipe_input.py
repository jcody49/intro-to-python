import pickle

# Function to take recipe input from the user
def take_recipe():
    name = input("Enter the name of the recipe: ")
    cooking_time = int(input("Enter the cooking time in minutes: "))
    ingredients = input("Enter ingredients (separated by a comma): ").split(", ")

    # Calculate difficulty based on cooking time and number of ingredients
    difficulty = calc_difficulty(cooking_time, len(ingredients))

    # Create a dictionary to store recipe information
    recipe_info = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients,
        'difficulty': difficulty
    }
    return recipe_info

# Function to calculate recipe difficulty
def calc_difficulty(cooking_time, num_ingredients):
    if cooking_time < 10 and num_ingredients < 4:
        return 'Easy'
    elif cooking_time < 10 and num_ingredients >= 4:
        return 'Medium'
    elif cooking_time >= 10 and num_ingredients < 4:
        return 'Intermediate'
    elif cooking_time >= 10 and num_ingredients >= 4:
        return 'Hard'

# Main code
filename = input("Enter the name of the file containing your recipe data: ")

try:
    with open(filename, 'rb') as file:
        data = pickle.load(file)
except FileNotFoundError:
    print(f"File {filename} not found.")
    # If the file is not found, create a new data dictionary
    data = {
        'recipes_list': [],
        'all_ingredients': []
    }

# Extract values from the dictionary into separate lists
recipes_list = data.get('recipes_list', [])
all_ingredients = data.get('all_ingredients', [])

n = int(input("How many recipes would you like to enter? "))

for i in range(n):
    # calls take_recipe() to get user input for the recipe
    recipe = take_recipe()

    # Update the all_ingredients list with unique ingredients from the current recipe
    for ingredient in recipe['ingredients']:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)

    recipes_list.append(recipe)

# Calculate recipe difficulties
for recipe in recipes_list:
    recipe['difficulty'] = calc_difficulty(recipe['cooking_time'], len(recipe['ingredients']))

# Display recipes
for recipe in recipes_list:
    print('Recipe:', recipe['name'])
    print('Cooking time (min):', recipe['cooking_time'])
    print('Ingredients:')
    for ingredient in recipe['ingredients']:
        print(ingredient)
    print('Difficulty:', recipe['difficulty'])

# Display all ingredients across all recipes
print('All Ingredients')
print('_______________')
for ingredient in all_ingredients:
    print(ingredient)

# Save the updated data to the file using pickle.dump
data = {
    'recipes_list': recipes_list,
    'all_ingredients': all_ingredients
}

with open(filename, 'wb') as file:
    pickle.dump(data, file)
