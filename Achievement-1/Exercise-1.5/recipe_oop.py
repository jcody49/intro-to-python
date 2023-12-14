class Recipe:
    all_ingredients = set()

    def __init__(self, name, ingredients, cooking_time):
        self.name = name
        self.ingredients = ingredients
        self.cooking_time = cooking_time
        self.difficulty = self.calculate_difficulty()

    def calculate_difficulty(self):
        difficulty = 'Hard'  # Default to the most complex case
        if self.cooking_time < 10:
            difficulty = 'Easy' if len(self.ingredients) < 4 else 'Medium'
        elif len(self.ingredients) < 4:
            difficulty = 'Intermediate'
        return difficulty

    def get_name(self):
        return self.name

    def set_name(self, name=""):
        self.name = name

    def get_cooking_time(self):
        return self.cooking_time

    def set_cooking_time(self, cooking_time=int):
        self.cooking_time = cooking_time

    # Method to add new ingredients to the ingredient list
    def add_ingredients(self, *ingredients):
        # Simple filter to avoid repeated items
        for ingredient in ingredients:
            if ingredient not in self.ingredients:
                self.ingredients.append(ingredient)

    def get_ingredients(self):
        return self.ingredients

    def get_difficulty(self):
        if self.difficulty is None:
            self.calculate_difficulty()
        return self.difficulty

    def search_ingredient(self, target_ingredient):
        return target_ingredient in self.ingredients

    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in Recipe.all_ingredients:
                Recipe.all_ingredients.add(ingredient)
                print("New ingredients have been added:", ingredient)

    def __str__(self):
        output = "\nName: " + str(self.name) + \
                 "\nCooking Time: " + str(self.cooking_time) + \
                 "\nIngredients: " + ', '.join(self.ingredients) + \
                 "\nDifficulty: " + str(self.difficulty)
        return output

def recipe_search(data, search_term):
    # Search for recipes containing a specific ingredient
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe)


# Create a list of Recipe objects
recipes_list = []

tea = Recipe("Tea", ["Tea Leaves", "Sugar", "Water"], 5)
coffee = Recipe("Coffee", ["Coffee Powder", "Sugar", "Water"], 5)
cake = Recipe("Cake", ["Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk"], 50)
banana_smoothie = Recipe("Banana Smoothie", ["Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes"], 5)

# Append the objects to the list after they are defined
recipes_list.extend([tea, coffee, cake, banana_smoothie])


result = tea.search_ingredient("Sugar")

print(result)


# Display the string representations of the recipes in the list
for recipe in recipes_list:
    print(recipe)

# Search for recipes containing Water
print("\nRecipes containing Water:")
recipe_search(recipes_list, "Water")

print("\nRecipes containing Sugar:")
recipe_search(recipes_list, "Sugar")

print("\nRecipes containing Bananas:")
recipe_search(recipes_list, "Bananas")
