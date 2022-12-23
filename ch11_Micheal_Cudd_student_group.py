# Micheal Cudd
# Module 11 Programming Assignment
# Part A
# Random group of students to work on a project.
#
# Create a program called student_group.py that the
# random module (https://docs.python.org/3.5/library/random.htmlLinks to an external site.)
# to create a list of random students to work together on a group project, as follows:
#
#     Create a list of at least 10 student names.
#     Prompt the user to input how many students should be in the group.
#     Generate a random number appropriate to the number of names in the list
#     Use the random number to retrieve and print the corresponding name from the list.
#     Repeat until you have output the correct number of students, as input by the user.
#
# Note: This program will have a flaw--the same student could be chosen multiple times.
# Although you can solve this issue if you want, you are not required to address it for the assignment.

import random

# student list
students = ['Nathalie', 'Ximena', 'Dayanna', 'Athena', 'Kimberly',
'Jazmin', 'Vanezia', 'Michelle', 'Jazlyne', 'Frances']

group = int(input("How many students are in the group? "))

# option 1, will contain duplicate names at times
# for i in range(group):
    # print(random.choice(students))

# option 2, should not contain duplicate names
print(random.sample(students, group))