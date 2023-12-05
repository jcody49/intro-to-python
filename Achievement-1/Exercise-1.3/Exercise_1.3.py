recipes_list = []

ingredients_list = []

def take_recipe() :
    name = input("Enter the name of the recipe: ")
    cooking_time = int(input("Enter the cooking time in minutes: "))

    ingredients = input("Enter ingredients (separated by a comma): ").split(", ")
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients
    }
    return recipe

n = int(input("How many recipes would you like to enter? "))

for i in range(n):          #runs n times
    recipe = take_recipe()          # a recipe gets assigned to the recipe variable via the take_recipe function
    for ingredient in recipe['ingredients']:        # for loop iterates over each ingredient in the ingredients list
        
        # checks if ingredient is already present in list and appends it to the list if it is not already present
        if not ingredient in ingredients_list:       
            ingredients_list.append(ingredient)
    recipes_list.append(recipe) 
    

for recipe in recipes_list:
    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
        recipe['difficulty'] = 'Easy'
    elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
      recipe['difficulty'] = 'medium'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
      recipe['difficulty'] = 'intermediate'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) >= 4:
      recipe['difficulty'] = 'hard'

for recipe in recipes_list:
   print('Recipe:', recipe['name'])
   print('Cooking time (min):', recipe['cooking_time'])
   print('Ingredients:')
   for ingredient in recipe['ingredients']:
      print(ingredient)
   print('Difficulty:', recipe['difficulty'])


def print_ingredients():
   ingredients_list.sort() # alphabetizes
   print('All Ingredients')
   print('_______________')
   for ingredient in ingredients_list:
     print(ingredient)

print_ingredients()

