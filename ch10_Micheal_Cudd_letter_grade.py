# Micheal Cudd
# Module 10 Programming Assignment
# Part B

# This program calculates grade based on a percentage.

# Create a program called letter_grade.py that asks the user to input their current grade percentage and
# then outputs the corresponding letter grade (A through F).
#
# Within a try-except structure raise (not just catch) two different exceptions:
# one if the user inputs a grade of less than zero and a different exception if
# the user inputs a grade greater than 100. Be sure to also handle input that is not a number.
#
# Note that you can use a ValueError (as described in zyBooks 10.3) and
# do not need to create a custom exception (as described in 10.6).

#grade percentage
# A	90 – 100
# B	89 – 80
# C	79 – 70
# D	69 – 65
# F	64 – 0

#used Tracy's code for the beginning. Now print letter input error but get TypeError for over/under error
choice = ''
while choice != 'Q':
    try:
        grade = input("What is your grade percentage? ")

        try:
            grade = int(grade)
        except ValueError:
            print("Please enter a grade from 0 to 100. ")
            continue # fixed TypeError, but keeps going.

    # error check
        if grade > 100:
            raise ValueError("You cannot have a grade over 100%")
        if grade < 0:
            raise ValueError("You cannot have a grade less than zero")
        # if not grade:
        #     raise TypeError("Please enter a number between 0 and 100")

    # tried for catching letters instead of numbers:
    # if grade is not grade.isdigit():
    # if grade != grade.isdigit():
    # if grade == grade.isalpha():
    # if not grade:
    # if not grade.isdigit():
    # TypeError and ValueError


    # grade check
        if grade == 100:
            print('Excellent that is an A')
        if grade >= 90 and grade <= 99:
            print('That grade is an A')
        if grade >= 80 and grade <= 89:
            print('That grade is an B')
        if grade >= 70 and grade <= 79:
            print('That grade is an C')
        if grade >= 65 and grade <= 69:
            print('That grade is an D')
        if grade >= 0 and  grade <= 64:
            print('That grade is an F')

        # doesnt work.
        # else:
        #     print("Please enter a number between 0 and 100")


    # If percentage is less than 0 or greater than 100
    except ValueError as error:
            print(error)

    # overwrites raise error if first doesnt get called if second
    # except ValueError:
    #     print("Please enter a number between 0 and 100")

    # except TypeError:
    #     print("opps")

# does not quit on Q.
choice = input('Enter Q to quit, anything else to do it again: ').upper()