# Micheal CUdd
# Module 05 Programming Assignment
# Part A

# This program gives a sum of numbers inside a range.



# Create a program called sum_loop.py. In it, ask the user for a starting number and an ending number.
# Then use a loop (not a function) to calculate the sum of every number from the first to the second.
# The image below shows an example of the user inputs 3 and 15.


# number inut from user
starting_number = int(input('What is your starting number? '))
ending_number = int(input('What is your ending number? ')) + 1
sum = 0

# loop to do the sum

for i in range(starting_number, ending_number):
    sum += i

print(sum)




