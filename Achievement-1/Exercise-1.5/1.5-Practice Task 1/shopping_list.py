class ShoppingList:
    def __init__(self, list_name):
        self.list_name = list_name
        self.shopping_list = []

    def add_item(self, item):
        if item not in self.shopping_list:
            self.shopping_list.append(item)
            print(f"{item} added to the shopping list.")
        else:
            print(f"{item} is already in the shopping list.")

    def remove_item(self, item):
        if item in self.shopping_list:
            self.shopping_list.remove(item)
            print(f"{item} has been removed from the shopping list.")
        else:
            print(f"{item} does not exist on this list.")

    def view_list(self):
        print(f"{self.list_name} Shopping List:")
        for item in self.shopping_list:
            print(f"- {item}")

# Create an object called pet_store_list from this class. Set its list_name as Pet Store Shopping List during initialization.
pet_store_list = ShoppingList("Pet Store Shopping List")

# add the following
pet_store_list.add_item("Dog Food")
pet_store_list.add_item("Frisbee")
pet_store_list.add_item("Bowl")
pet_store_list.add_item("Collars")
pet_store_list.add_item("Flea Collars")

# Remove flea collars using the remove_item() method.
pet_store_list.remove_item("Flea Collars")

# Try adding frisbee again using the add_item() method.
pet_store_list.add_item("Frisbee")

# Display the entire shopping list through the view_list() method.
pet_store_list.view_list()