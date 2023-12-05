destination_list = ["Denver", "L.A.", "Colorado Springs"]
destination = input("Where would you like to travel? ")

if destination in destination_list:
    print("Enjoy your stay in " + destination + "!")
else:
    print("Oops, that destination is not currently available.") 