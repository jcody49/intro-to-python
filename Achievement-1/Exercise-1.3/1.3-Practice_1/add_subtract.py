a = int(input("Enter a number: "))
symbol = str(input("Enter + for additon or - for subtraction: "))
b = int(input("Enter another number to be added to or subtracted from the first: "))


if symbol == "+" :
    print("The sum of these numbers is " + str(a + b))
elif symbol == "-" :
    print("The difference between these numbers is " + str(a-b))
else: 
    print("Make sure that you have entered the correct symbol")