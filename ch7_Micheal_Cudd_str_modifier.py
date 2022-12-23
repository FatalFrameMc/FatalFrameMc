# Micheal Cudd
# Module 07 Programming Assignment
# Part B

# This program team and city.

# Create a program that accept a the name of a sports team--including city--and
# then convert it to all uppercase with underscore characters in place of any spaces; output the result.
# Be sure to give the user adequate instructions for using the program. Name the file str_modifier.py.
# Sample Program Run:
#
# Enter your full name: New York Yankees
# The new version of this name is NEW_YORK_YANKEES

# check 7.3 7.4

# user input city and team
what_city = input('What city is your team from? ')
what_team = input('What is your teams name? ')



new_city = what_city.replace(' ', '_')
new_team = what_team.replace(' ', '_')

team2 = '_'.join([new_city, new_team]).upper().strip()

print(f'{team2}')
