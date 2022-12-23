# Micheal Cudd
# Module 08 Programming Assignment
# Part B

# This program course list dictionary with 7 courses. Course Names and Instructors.

# Create a program called courses.py that has a dictionary with 7 course names (for example: CIS105, ENG101, etc),
# along with the name of each associated instructor.
# Prompt the user for the name of a course to look up, or the word "quit" to exit.
# After the user types in a course, it should look up and print that course's instructor.
#
# The program should repeat this until the user enters "quit" at the prompt.
#
# Note: The program does NOT need to gracefully handle the error that may occur
# if the course is not found in the dictionary; for now,
# your program only needs to work when a course is entered correctly.

#My Courses, ones I have taken and looking to take or will take.
courses = {
    "CIS156" : "T. Baker",
    "CIS126RH" : "T. Baker",
    "ITS240" : "A. Dezilva",
    "BPC270" : "G. Olson",
    "CIS271DB" : "T. Polliard",
    "ENH251" : "R. Freeman",
    "ART131" : "J. Fike"
}

#User input
# course_lookup = input("What course does you want to look for? ").upper()

# if course_lookup in course_lookup:
#     print(courses.keys(), courses.values(), end='')

# course look up and exit on quit

print('Course available CIS156,CIS126RH,ITS240, BPC270, CIS271DB, ENH251, ART131. When finished please enter QUIT to exit. ')

while True:
    course_lookup = input("What course does you want to look for? ").upper()
    for k, v in courses.items():
        if k == course_lookup:
            print(f'Your class is {k} the Instructor is {v}')
        if course_lookup == 'QUIT':
            print("Bye")
            exit()

