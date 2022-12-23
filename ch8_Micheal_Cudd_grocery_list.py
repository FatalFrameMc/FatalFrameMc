# Micheal Cudd
# Module 08 Programming Assignment
# Part A

# This program grocery list and number of items.

# Create a program called grocery_list.py that allows the user to input a list of items to buy at the supermarket.
# It should begin by asking the user to input the number of items to add to the list.
# Then, it should use a loop to prompt the user to input that many items, storing each in the list.
#
# After the items have been entered, it should output the full list.

# what groceries and how many

item_number = int(input("how many items do you want to add to your list? "))

# grocery list
grocery_list = []

# number of iterations from user input
for i in range(item_number):
    groceries = input("what would you like to add? ")
    # how_many = input("how many items would you like to add? ")

# add items to groceries list.
    grocery_list.append(groceries)

print(grocery_list)
