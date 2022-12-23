# Micheal Cudd
# Module 12 Programming Assignment
# Part A
# This program allows a user to select a line of a text file and read that line.

# Create a program called read_file.py that reads the address.txt file linked below into a list.
# Then, prompt the user to enter a line number, and display that line from the file.
# Keep repeating until the user decides to exit.


# import file
address = open('address.txt')
# get from user
print("Please make sure address.txt is in the same directory as this program.")
line = input("Enter a line number 1-12. Q to exit. ")
# # read the file
content = address.readlines()
# #print the line/s
# print(content[line -1])

while line != 'Q':
    line = int(line)
    # content = address.readlines()
    print(content[line - 1])
    line = int(input("Enter a line number 1-12. Q to exit. "))

print('Thank you for reading.')