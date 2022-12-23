# Micheal Cudd
# Module 10 Programming Assignment
# Part A

# This program calculates paint cost with 1 try and 2 except statements.

# Create a program called paint_cost.py that prompts the user to input
# the height of a wall (in feet),
# the width of the wall (in feet), and
# the cost of the paint used to cover it.
# Output the area of the wall (height x width) and the cost per square foot (cost / area).
#
# Use try and at least two except statements to handle issues that arise if the user
# does not input numbers or enters zero as the area, outputting a relevant message for each issue.


try:
    wall_height = float(input('Wall Height in feet? '))
    wall_length = float(input('Wall Length in feet? '))
    paint_cost = float(input('Paint Cost per square foot? '))

    area = wall_height * wall_length
    print(f' The area of the wall is {area}')

    cost = float(paint_cost) / float(area)
    print(f' The cost to paint per square foot is {cost}')

# Error checks for text as numbers and wall size is greater than 0
except ValueError:
    print("Input must be a number.")
except ZeroDivisionError:
    print('Wall size must be greater than 0.')


finally:
    print("Thank you.")

# if wall_height and wall_length and paint_cost >= 1:
#     print(f' the wall area is {wall_height * wall_length}')
#     print(f'the cost to paint is {(wall_height * wall_length) / paint_cost}')
# if wall_height or wall_length or paint_cost <= 0:
#     raise ValueError