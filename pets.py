# Micheal Cudd
# Module 13 Programming Assignment
# Part A
# Pets.

# Create a program called pets.py that that defines a pet class with at least three general attributes (fields)
# for all pets (for example, name, age, etc.) and at least two functions/behaviors for all pets
# (for example, eating). The functions can simply print something.
#
# Next, create two derived classes from the base class that represent specific types of pets. For example,
# one derived class might be a dog. Add at least one attribute/field and at least two functions/behaviors
# specific to that kind of pet.
#
# Finally, demonstrate that both derived classes work by creating at least one instance of
# each and showing off their fields and functions.
#
# Note: In preparation for the Final Project, this assignment leaves room for you to make more
# decisions about the code than previous assignments.
# Just be sure that your submission demonstrates the key concepts from the chapter, as indicated in these directions.

###############################

# pet class with 3 fields - IE: name, age, type
# 2 functions/behaviors - IE: eating
class Pets:
    def __init__(self):
        self.name = ''
        self.age = 0
        self.breed = ''

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_type(self, breed):
        self.breed = breed


# derived class 1 - specific type of pet with specifics as above
class Dog(Pets):
    def __init__(self):
        Pets.__init__(self)
        self.trick = ''
        self.diet = 'Dog food'

    def dog_trick(self):
        self.trick = 'Fetch'
        self.trained = 'Guard and protection trained'


# derived class 2 - specific type of pet with specifics as above
class Cat(Pets):
    def __init__(self):
        Pets.__init__(self)
        self.trick = ''
        self.diet = 'Cat food'

    def cat_trick(self):
        self.trick = 'Scratching Post'
        self.trained = 'Litter Box Trained'