# Micheal Cudd
# Module 11 Programming Assignment
# Part B
# Math Module with factorial and power of 3.


# Create a program called math_module.py that uses the
# math module (https://docs.python.org/3.5/library/math.htmlLinks to an external site.) to do the following:
#
# Prompt the user to enter a number.
# Calculate and output the factorial of the entered number using a function from the math module.
# For example, the factorial of 4 is 24.
# Calculate and output the value of the entered number raised to the power of 3 using a function from the math module.
# For example, 4 raised to the power of 3 is 64.
#
# Hint: You may find the w3schoolsLinks to an external site. math module reference helpful in solving Part B.

import math

try:
    user_number = input("Please enter a number. ")

    try:
        user_number = int(user_number)
    except ValueError:

# process
     if user_number < 0:
        raise ValueError
    if user_number >= 1:
        print(f' Your factorial number is: {math.factorial(user_number)}') # has to be positive non-float number int
        print(f' Your number to the power of 3 is: {math.pow(user_number, 3)}') # can be negitive and a float

except:
    print("Please enter a whole positive number.")

finally:
    print()



# user_number = int(input("Please enter a whole number. "))

# has to be positive number int
# print(math.factorial(user_number))
# can be negitive
# print(math.pow(user_number, 3))