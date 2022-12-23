# Micheal Cudd
# Module 05 Programming Assignment
# Part B

# This program valid age input from user.

# Create a program called valid_input.py. In a loop, prompt the user to input their age in years;
# keep prompting until the user inputs a number greater than zero and less than 100.
# Once the user has input a valid number, output "Thank you,"

# Age input from user
age = int(input("What is you age? "))
# for age in range(1, 101):
#     if age > 0 or age < 100:
#         print('Thank you.', age, 'is a valid age')
#     continue


while age < 1 or age > 100:
    age = int(input("What is you age? "))

print('Thank you.', age, 'is a valid age')
