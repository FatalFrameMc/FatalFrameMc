# Micheal Cudd
# Final
# This program creates a dice roller for dice based games

# all of
# a function that accepts at least one argument  <-- Random Character
# a function that returns a value (which can be same function as above)  <-- Random Character
# uses a loop in a meaningful way  <-- dice roller
# basic exception handling using try and except  <-- dice roller
#
# and at least one of the following, each in a meaningful way:
# uses a class
# uses a list or dictionary <-- Random Character
# reads / writes to files <-- working on for Random Character
###################################################################
import random
# print('Error code, and input of non integer not working')

choice = ''
while choice != 'n':
    total = 0
    try:
        how_many = input('How many dice do you want to roll? ')
        sides = input('How many sides are on the die? (2 or more sides)? ')

        try:
            how_many = int(how_many)
        except ValueError:
            print('Please enter a number.')
            continue
        try:
            sides = int(sides)
        except ValueError:
            print('Please enter a number.')
            continue


    # Error Check
        if how_many <= 0:
            raise ValueError('You must roll at least 1 time.')
        if sides < 2:
            raise ValueError('Dice must have at lease 2 sides.')

        # Roll
        for i in range(how_many):
            how_many = random.randint(1, sides)
            total = total + how_many
            print("roll ", i+1, "=", how_many)
            print("Total =", total)

        choice = input("Do you want to roll again. (Y/N) ")
        if choice.lower() == 'n':
            break

    except ValueError as error:
        print(error)
