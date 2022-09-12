# Micheal Cudd
# Module 03 Programming Assignment
# Part B

# Dictionary of names and age of family.


#Create a program named family.py with a dictionary of names and ages for a family of at least four people;
# this may be your family or a fictional family (such as the Simpsons). Print out the dictionary.
# Then, print just the age of the 2nd person in the dictionary.
# Next, add an entry for "Tim" with the age 23 (without changing or re-creating the existing dictionary data),
# and print the full dictionary again.

#Finally, prompt the user for a name to look up, and then output that person's age.

#family dictionary
family = {
    'Daenerys Targaryen': 13,
    'Jon Snow': 14,
    'Arya Stark': 9,
    'Tyrion Lannister': 24,
    'Ygritte': 18
}

#whole list
print(family)

#age of second
print(family.get('Jon Snow'))

#add Tim and print whole dictionary
family['Tim'] = 23
print(family)

#who to look up
search = family.get(input("Who do you want to look for: "))
print(search)