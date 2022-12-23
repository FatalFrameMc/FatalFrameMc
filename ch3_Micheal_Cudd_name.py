#  Micheal Cudd
#  Module 03 Programming Assignment
#  Part A

#  Name, length of name, initials, and second to last name.




# Create a program named name.py that prompts the user to input their first name and stores it in a variable.
#  Then prompt the user for their last name, and store that in a second variable. Use their input to do each of the following:

# Create a variable with their full name (first and last, including a space between), and then print it
# Output the length of the full name variable
# Output the user's initials (first letter in the first name and first letter in the last name, each followed by a period)
# Output the second-to-last letter in the first name

# User input
first_name = input("First Name: ")
last_name = input("Last Name: ")

# assignment codes
full_name = first_name + " " + last_name
length = len(full_name)
# initials = first_name[0] + last_name[0]
second2last = first_name[-2]

# output
print("Your full name is:", full_name + '.')
print("Your name is", length ,"characters long.")
print('Your initials are:', first_name[0] + '.' + last_name[0] + '.')
print("The second to last letter of the first name is:", second2last + '.')