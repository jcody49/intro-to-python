import mysql.connector

#initialize connector object
conn = mysql.connector.connect(
   host='localhost',
   user='cf-python',
   passwd='password'
)

cursor = conn.cursor()

# Create database if not exists
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

# Use the task_database
cursor.execute("USE task_database")

# Commit the changes
conn.commit()



# Check if the table Recipes exists
cursor.execute("SHOW TABLES LIKE 'Recipes'")
table_exists = cursor.fetchone()

if not table_exists:
    cursor.execute('''CREATE TABLE Recipes(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        ingredients VARCHAR(255),
        cooking_time INT, 
        difficulty VARCHAR(20)
    )''')

    conn.commit()
else:
    print("Table 'Recipes' already exists.")


def calculate_difficulty(cooking_time, ingredients, column_to_update):
    difficulty = 'Hard'  # Default to the most complex case
    if column_to_update.lower() == 'cooking_time':
        if int(cooking_time) <= 10:
            difficulty = 'Easy' if isinstance(ingredients, list) and len(ingredients) < 4 else 'Medium'
        elif int(cooking_time) > 10 and isinstance(ingredients, list) and len(ingredients) < 4:
            difficulty = 'Medium'
    elif column_to_update.lower() == 'ingredients':
        if isinstance(ingredients, list) and len(ingredients) < 4:
            difficulty = 'Intermediate'
        else:
            difficulty = 'Easy'
    return difficulty








def create_recipe(conn, cursor):
    print("Create a new recipe:")
    name = str(input("Enter the name of the recipe:"))
    cooking_time = int(input("Enter the recipe's cooking time (in minutes):"))
    ingredients = [str(ingredient) for ingredient in input("Enter the recipe's ingredients, separated by commas: ").split(", ")]
    difficulty = calculate_difficulty(cooking_time, ingredients)

    ingredients_string = ", ".join(ingredients)

    cursor.execute('''
        INSERT INTO Recipes(name, ingredients, cooking_time, difficulty) 
        VALUES(%s, %s, %s, %s)
        ''', (name, ingredients_string, cooking_time, difficulty))

    conn.commit()




def search_recipe(conn, cursor):
    # executes a SELECT query on the Recipes TABLE 
    cursor.execute("SELECT ingredients FROM Recipes")
    # set automatically handles duplicates
    all_ingredients = set()  


    # retrieves all ingredients that have been loaded into the cursor
    results = cursor.fetchall()

    # iterates over each row in the ingredients col
    for recipe_ingredients_list in results:
        # Iterate through recipe_ingredients
        for recipe_ingredients in recipe_ingredients_list:
            # split each recipe ingredient
            recipe_ingredient_split = recipe_ingredients.split(", ")
            all_ingredients.update(recipe_ingredient_split)
        

    # Remove all duplicates from the list
    all_ingredients = list(dict.fromkeys(all_ingredients))      # creates a dictionary using the elements of all_ingredients as keys (since the keys are unique, duplicates are discarded), then list(...) converts the keys of the dictionary back into a list. 

    # Show all available ingredients in all_ingredients
    all_ingredients_list = list(enumerate(all_ingredients))


    print("\nAll ingredients list:")
    print("------------------------")


    for index, tup in enumerate(all_ingredients_list):      # iterates over the elements of all_ingredients_list; for each tuple generated by the enumerate function, an index is stored 
        print(str(tup[0]+1) + ". " + tup[1])        # prints a string formed by concatenating the modified index (index plus 1) and the ingredient name from the tuple.


    try:
        # creates obj that stores user input on their desired ingredient
        # which is then stored into a variable called ingredient_searched
        ingredient_searched_number = input("\nEnter the number that corresponds with your desired ingredient: ")

        # subtracts one from the ingredient_searched_number to reset the correct index value 
        ingredient_searched_index = int(ingredient_searched_number) - 1

        # the all_ingredients_list is searched for the requested ingredient via the second index ([1]) of the tuples
        ingredient_searched = all_ingredients_list[ingredient_searched_index][1]

        # once the desired ingredient is matched, it gets printed
        print("\nYou selected the ingredient: ", ingredient_searched)

    except:
        # if the searched_ingredient is not found, the following will be displayed
        print("An error occurred. Be sure to select a number from the list.")

    # the else block executes after the try block completes
    else:
        # Searches for rows in the table that contain search_ingredient within the ingredients column
        print("\nThe recipe(s) below include(s) the selected ingredient: ")
        print("-------------------------------------------------------")

        # performs query to SELECT from ingredients, searching for ingredient_searched in the ingredients col.
        # the '%' operator allows to match with any version of the ingredient_searched that has extra characters on either side of it  
        cursor.execute("SELECT * FROM Recipes WHERE ingredients LIKE %s", ('%' + ingredient_searched + '%', ))

        # fetches all ingredients that the query just loaded into the cursor (all ingredients matching or partially matching the ingredient_searched)
        results_recipes_with_ingredient = cursor.fetchall()

        # Displays the data from each recipe found
        for row in results_recipes_with_ingredient:
            print("\nID: ", row[0])
            print("name: ", row[1])
            print("ingredients: ", row[2])
            print("cooking_time: ", row[3])
            print("difficulty: ", row[4])

    conn.commit()
   


def update_recipe(conn, cursor):
    try: 
        # retrieve all recipes
        cursor.execute('''SELECT * FROM Recipes''')
        all_recipes = cursor.fetchall()

        # Displays all recipes
        for row in all_recipes:
            print("\nID: ", row[0])
            print("name: ", row[1])
            print("ingredients: ", row[2])
            print("cooking_time: ", row[3])
            print("difficulty: ", row[4])

        # Prompts user for a recipe id
        desired_recipe_id = int(input("Type the ID number that corresponds with your desired recipe: "))
        
        # finds the recipe whose id matches the desired_recipe_id and loads it into the cursor
        cursor.execute("SELECT * FROM recipes WHERE id = %s", (desired_recipe_id,))
        
        # loads the recipe in the cursor into a variable 
        selected_recipe = cursor.fetchone()

        if selected_recipe:
            print("\nSelected Recipe:")
            print("ID: ", selected_recipe[0])
            print("name: ", selected_recipe[1])
            print("ingredients: ", selected_recipe[2])
            print("cooking_time: ", selected_recipe[3])
            print("difficulty: ", selected_recipe[4])

            # Ask the user to select a column to update
            column_to_update = input("Type the column to be updated (name, cooking_time, ingredients): ")

            # Ask the user for the new value
            new_value = input(f"Enter the new value for {column_to_update}: ")


            # Convert cooking_time to an integer if it's the column being updated
            if column_to_update == "cooking_time":
                new_value = int(new_value)


            # Builds the update query, which will select the column to update based off of the id that the user input 
            update_query = f"UPDATE recipes SET {column_to_update} = %s WHERE id = %s"

            # runs the update query, replacing the old value with new_value in the row with the desired_recipe_id
            cursor.execute(update_query, (new_value, desired_recipe_id))

            # If the user updates cooking_time or ingredients, recalculate difficulty and update
            if column_to_update in ["cooking_time", "ingredients"]:
                # Recalculate difficulty using the updated cooking_time or ingredients
                # checks to see if the values have been updated
                # if yes it uses the new values; if no, it uses the original values
                new_difficulty = calculate_difficulty(selected_recipe[3] if column_to_update == "cooking_time" else new_value, selected_recipe[2] if column_to_update == "ingredients" else new_value, column_to_update)


                # Update difficulty in the database
                cursor.execute("UPDATE recipes SET difficulty = %s WHERE id = %s", (new_difficulty, desired_recipe_id))


            print("Recipe updated successfully!")

            # Display the updated information
            cursor.execute("SELECT * FROM recipes WHERE id = %s", (desired_recipe_id,))
            updated_recipe = cursor.fetchone()
            print("\nUpdated Recipe:")
            print("ID: ", updated_recipe[0])
            print("name: ", updated_recipe[1])
            print("ingredients: ", updated_recipe[2])
            print("cooking_time: ", updated_recipe[3])
            print("difficulty: ", updated_recipe[4])

            conn.commit()


        else:
                print("Recipe not found.")
                conn.commit()


    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        conn.commit()

        


   
def delete_recipe(conn, cursor):
    try:
        # Retrieve all recipes
        cursor.execute('''SELECT * FROM Recipes''')
        all_recipes = cursor.fetchall()

        # Display all recipes
        for row in all_recipes:
            print("\nID: ", row[0])
            print("name: ", row[1])
            print("ingredients: ", row[2])
            print("cooking_time: ", row[3])
            print("difficulty: ", row[4])

        # Prompt user for a recipe id to delete
        recipe_to_delete_id = int(input("Type the ID number of the recipe you want to delete: "))

        # Build the delete query
        delete_query = "DELETE FROM Recipes WHERE id = %s"

        # Execute the delete query
        cursor.execute(delete_query, (recipe_to_delete_id,))

        # Commit the changes
        conn.commit()

        print("Recipe deleted successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        conn.commit()




def main_menu(conn, cursor):
    try:
        while True:
            print("\nMain Menu:")
            print("1. Create Recipe")
            print("2. Search Recipe")
            print("3. Update Recipe")
            print("4. Delete Recipe")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                create_recipe(conn, cursor)
            elif choice == "2":
                search_recipe(conn, cursor)
            elif choice == "3":
                update_recipe(conn, cursor)
            elif choice == "4":
                delete_recipe(conn, cursor)
            elif choice == "5":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Commit changes and close connection after the loop
        conn.commit()
        conn.close()






# MAIN CODE

main_menu(conn, cursor)