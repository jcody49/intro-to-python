import pickle

recipe = {
    "Recipe_Name": "Tea",
    "Ingredients": ["Tea leaves", "Water", "Sugar"],
    "Cooking Time": "5 minutes",
    "Difficulty": "Easy"
}

with open('recipe_binary.bin', 'wb') as file:
    pickle.dump(recipe, file)

with open('recipe_binary.bin', 'rb') as file:
    loaded_recipe = pickle.load(file)

# Display the loaded recipe with readable formatting
print("Loaded Recipe:")
print(f"Recipe Name: {loaded_recipe['Recipe_Name']}")
print(f"Ingredients: {', '.join(loaded_recipe['Ingredients'])}")
print(f"Cooking Time: {loaded_recipe['Cooking Time']}")
print(f"Difficulty: {loaded_recipe['Difficulty']}")