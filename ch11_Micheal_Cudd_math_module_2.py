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


def factorial(user_number):
    try:
        if user_number < 0:
            raise ValueError
        else:
            return math.factorial(user_number)
    except:
        print('Please use a whole positive number for factorial.')

def pow_3(user_number):
   return math.pow(user_number, 3)


print('For factorial use a whole positive number. For power of 3 enter any number.')
user_number = int(input('Enter your number. '))


# has to be positive non-float number int
print(f' Your factorial number is: {factorial(user_number)}')
# can be negitive and a float
print(f' Your number to the power of 3 is: {pow_3(user_number)}')