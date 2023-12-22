# import the create_engine function from SQLAlchemy
from sqlalchemy import create_engine

# returned engine object
engine = create_engine("mysql+pymysql://cf-python:password@localhost/task_database")

# create a session on your database, import sessionmaker() from SQLAlchemy
from sqlalchemy.orm import sessionmaker

# connect session to the engine
Session = sessionmaker(bind=engine)

# initialize the session object
session = Session()

# function from SQLAlchemy that generates the declarative base class
from sqlalchemy.ext.declarative import declarative_base

# generate the class from this function
Base = declarative_base()


from sqlalchemy import Column
from sqlalchemy.types import Integer, String

# declaring new class
class Recipe(Base):
    # define what your table will be called in the database
    __tablename__ = "final_recipes"

    # data model
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    # add a __repr__ method to this class to help identify your objects easily from the terminal
    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + "-" + self.difficulty + ">"

    # Define a __str__ method that prints a well-formatted version of the recipe
    def __str__(self):
        formatted_recipe = (
            f"Recipe ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Ingredients: {self.ingredients}\n"
            f"Cooking Time: {self.cooking_time} minutes\n"
            f"Difficulty: {self.difficulty}"
        )
        print("=" * 35, end="\n")  # prints the dashed line 
        print(formatted_recipe, end="")  # prints formatted recipe 
        return formatted_recipe

    # calculate difficulty function
    def calculate_difficulty(self):
        num_of_ingredients = len(self.return_ingredients_as_list())

        if self.cooking_time < 10 and num_of_ingredients < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and num_of_ingredients >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and num_of_ingredients < 4:
            self.difficulty = "Intermediate"
        elif self.cooking_time >= 10 and num_of_ingredients >= 4:
            self.difficulty = "Hard"

    # retrieves the ingredients string inside your Recipe object as a list
    def return_ingredients_as_list(self):
        # If the instance variable self.ingredients is an empty string, return an empty list.
        if self.ingredients == "": return []
        # use the split() method available to strings to split the string into a list wherever there’s a comma followed by a space
        return self.ingredients.split(", ")


Base.metadata.create_all(engine)



# FUNCTIONS for main menu


def create_recipe():

    while True:     
        # gets user input for recipe name
        name = str(input("Enter recipe name: "))
        # if name is greater than 50, error message will occur
        if len(name) > 50:
            print("Name is too long, please enter a name with a maximum of 50 characters including spaces.")
        else: break

    # get cooking time
    while True:
        cooking_time_input = input("Enter cooking time in minutes: ")
        if not cooking_time_input.isnumeric():      # checks to make sure the cooking time is a number
            print("This is not a number. Please enter minutes as a number.")
        # if it is a number, the cooking time is set from the user's input
        else:
            cooking_time = int(cooking_time_input) 
            break


    # Collect ingredients

    # initialize ingredients_list
    ingredients_list = []
    # Ask the user how many ingredients they’d like to enter.
    while True:
        # ensures the user enters an int
        try:
            num_ingredients = int(input("How many ingredients would you like to enter? "))
            break
        except ValueError:
            print("Please enter a valid number.")

    # Based on this number, run a for loop that collects each ingredient and then adds it to your temporary list, ingredients.
    for _ in range(num_ingredients):
        ingredient = str(input("Type ingredient: "))
        ingredients_list.append(ingredient)
    # generate recipe obj that takes the users input from the previous prompts and suppllies the parameters for the recipe instance
    recipe_entry = Recipe(name=name, ingredients=", ".join(ingredients_list), cooking_time=cooking_time)

    recipe_entry.calculate_difficulty()
    # adds Recipe object to the database
    session.add(recipe_entry)
    session.commit()



def view_all_recipes():
    # Query all recipes from the database
    all_recipes = session.query(Recipe).all()

    if len(all_recipes) < 1:
        print("There are no entries in the database.")
        return None

    # Loop through the list of recipes, and the print function automatically looks for the __str__ method of an object
    for recipe in all_recipes:
        print(recipe)






# Search for recipes by ingredient

def search_by_ingredients():
    # Check if any recipes exist in the database
    if session.query(Recipe).count() < 1:
        print("There are no entries.")
        return
    # Retrieve only the values from the ingredients column
    results = session.query(Recipe.ingredients).all()

    # Initialize an empty list called all_ingredients.
    all_ingredients = []

    # Convert strings into list and remove duplicates
    for instance in results:
        ingredient_list = instance[0].split(", ")       # split up the ingredients into a temporary list 
        # add each ingredient from this list to all_ingredients
        for ingredient in ingredient_list:
            # Check each ingredient isn’t already on the list before adding.
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)



    # Print all ingredients
    for count, ingredient in enumerate(all_ingredients):
        print(f"{count}. {ingredient}")

    # Ask the user by which ingredients they’d like to search for recipes
    ingredients_input = input("Enter the numbers that corresponds with your desired ingredients, separated by spaces: ")        # The user is allowed to pick these ingredients by typing the numbers corresponding to the ingredients, separated by spaces.
    ingredient_nums = ingredients_input.split(" ")
    search_ingredients = []


    # Check that the user’s inputs match the options available
    for ingredient_num in ingredient_nums:
        if not ingredient_num.isnumeric():      # ingredient_num must be numeric inpput
            print("Input is not valid!")
            return
        else: ingredient_num = int(ingredient_num)
        if ingredient_num < 0 or ingredient_num >= len(all_ingredients): #num must be within displayed range
            print("Invalid input! Please enter a valid number within the range.")
            return
        # make a list of ingredients to be searched for, called search_ingredients
        search_ingredients.append(all_ingredients[int(ingredient_num)])



    # Search for recipes containing the desired ingredients
    conditions = []     # Initialize an empty list called conditions     
    for search_ingredient in search_ingredients:
        like_term = "%" + search_ingredient + "%"       # defines like_term obj to find the search_ingredient substring within the whole search_ingredients string 
        conditions.append(Recipe.ingredients.like(like_term))       # any matching substrings (like_terms) from the entire ingredients col will be appended to the conditions list
    recipes = session.query(Recipe).filter(*conditions).all()       # filter uses the conditions list to find any recipes that match the specified ingredients, then loads all of those recipes into the recipe object
    # Print all resulting recipes
    if not recipes:
        print("No recipes found with the selected ingredients.")
    else:
        for recipe in recipes:
            print(recipe)





def edit_recipe():
    # Check if any recipes exist in the database
    if session.query(Recipe).count() < 1:
        print("There are no recipes in the database!")
        return
    # Retrieve the recipes and their entities (id and name) from the database
    results = session.query(Recipe).with_entities(Recipe.id, Recipe.name).all()

    # Print recipe IDs and names
    ids = []        # Initializes an empty list called ids to store the recipe IDs 
    for recipe in results:
        # for each recipe, the recipe id and recipe name is printed
        print(recipe[0], recipe[1])
        ids.append(recipe[0])       # adds the recipes to the end of the ids list

    # Get ID of recipe from user
    try:
        # The user gets to pick a recipe by its id. 
        id = int(input("Please enter the ID of the recipe that you want to update and hit enter: "))        #The user gets to pick a recipe by its id. If the chosen id doesn’t exist, exit the function
    # If the chosen id isn't a number
    except:
        print("Input is invalid! Going back to main menu.")
        return

    # Check ID
    if not id in ids:
        print("ID not found! Going back to main menu.")     # If the chosen id doesn’t exist, exit the function
        return
    # Retrieve the entire recipe that corresponds to this id from the database into a variable called recipe_to_edit
    recipe_to_edit = session.query(Recipe).filter(Recipe.id == id).one()
    # Display the recipe, including only name, ingredients and cooking_time. Display a number next to each attribute so that the user gets to pick one.
    print("1 - Name:", recipe_to_edit.name)
    print("2 - Ingredients:", recipe_to_edit.ingredients)
    print("3 - Cooking time", recipe_to_edit.cooking_time)
    # Let user select property to update
    try:
        # Ask the user which attribute they’d like to edit by entering the corresponding number.
        num = int(input("Enter the corresponding number of the attribute that you'd like to edit: "))
    # check the user’s input
    except:
        print("Input is invalid! Going back to main menu.")
        return
    # if-else statements are used to edit the respective attribute inside the recipe_to_edit object
    if num == 1:
        # Edit name
        while True:
            # takes user input to replace the recipe name
            name = str(input("Enter new recipe name: "))
            # ensures the length is less than 50 chars
            if len(name) > 50:
                print("Name is too long, please enter a name with a maximum of 50 characters including spaces.")
            else: break
        # while loop ends and the name in the recipe_to_edit obj, is replaced by the name entered by the user
        recipe_to_edit.name = name
    # Edit ingredients
    elif num == 2:
        ingredients_list = []
        while True:
            ingredient = str(input("Enter new ingredient or hit enter if done: "))
            if ingredient != "":
                ingredients_list.append(ingredient)
            else: break
        ingredients = ", ".join(ingredients_list)
        recipe_to_edit.ingredients = ingredients
        recipe_to_edit.calculate_difficulty()
    # Edit cooking time
    elif num == 3:
        while True:
            cooking_time_input = input("Enter new cooking time in minutes: ")
            if not cooking_time_input.isnumeric():
                print("This is not a number. Please enter minutes as a number.")
            else:
                cooking_time = int(cooking_time_input)
                break
        recipe_to_edit.cooking_time = cooking_time
        recipe_to_edit.calculate_difficulty()
    else:
        print("Number is invalid! Going back to main menu.")
        return
    # Commit changes
    session.commit()



def delete_recipe():
    # Check if any recipes exist on database
    if session.query(Recipe).count() < 1:
        print("There are no recipes in the database!")
        return

    # Get all recipe names and IDs from database
    results = session.query(Recipe).with_entities(Recipe.id, Recipe.name).all()
    # Retrieve the id and name of every recipe in the database. List these out to the user to choose from.
    ids = []
    for recipe in results:
        print(recipe[0], recipe[1])
        ids.append(recipe[0])

    # Get ID of recipe from user
    try:
        # Ask the user which recipe they’d like to delete by entering the corresponding id
        delete_num = int(input("Enter the id number for the recipe you would like to delete: "))
    # Verify inputs
    except:
        print("Input must be a number! Going back to main menu.")
        return

    # Check ID
    if delete_num not in ids:
        print("ID not found! Going back to main menu.")
        return
    # Based on the selected id, retrieve the corresponding object that exists in the database
    recipe_to_delete = session.query(Recipe).filter(Recipe.id == delete_num).one()

    print(recipe_to_delete)
    # Ask the user if they’re sure that they’d like to delete this entry. If it’s a ‘yes’, perform the delete operation and commit this change. Otherwise, exit the function.
    answer = input("Are you sure to delete this recipe? (If yes, enter 'yes' and hit enter): ")
    if answer == "yes":
        session.delete(recipe_to_delete)
        session.commit()
        print("Recipe deleted!")






# MAIN MENU LOOP

# Initialize an empty string to store the user's choice
choice = ""

# Continue looping until the user chooses to quit
while (choice != "quit"):
    # Display the main menu options
    print("\nMAIN MENU")
    print("=" * 50)
    print("Pick a choice:")
    print("\t1. Create a new recipe")
    print("\t2. View all recipes")
    print("\t3. Search for a recipe by ingredients")
    print("\t4. Update an existing recipe")
    print("\t5. Delete a recipe")
    print("\tType 'quit' to exit the program")

    # Prompt the user to enter their choice
    choice = input("Your choice: ")

    # Perform actions based on user's choice
    if choice == "1": create_recipe()
    elif choice == "2": view_all_recipes()
    elif choice == "3": search_by_ingredients()
    elif choice == "4": edit_recipe()
    elif choice == "5": delete_recipe()
    elif choice != "quit": print("Invalid input!")

# End: Closing session and database
session.close()
engine.dispose()