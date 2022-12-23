# Micheal Cudd
# Module 06 Programming Assignment
# Part A
# This program totals the value of cash in a wallet.

# Create a program called total_cash.py that determines the total value of a wallet full of cash.
# It should ask the user to input the quantity of each denomination of bills (ones, fives, etc--up to hundreds).
# It should then call a function that accepts each of those values as arguments/parameters and returns (not prints!)
# the total amount of the cash. Finally, you should output the total value for the user to see.
#
# For example, if a user has 3 ones, 3 tens, and 1 fifty, their total is $83 in cash.

ones = int(input("How many ones? "))
fives = int(input("How many fives? "))
tens = int(input("How many tens? "))
twenties = int(input("How many twenties? "))
fifties = int(input("How many fifties? "))
hundreds = int(input("How many hundreds? "))

def total_cash(ones, fives, tens, twenties, fifties, hundreds):
    ones *= 1
    fives *= 5
    tens *= 10
    twenties *= 20
    fifties *= 50
    hundreds *= 100
    return ones + fives + tens + twenties + fifties + hundreds

print(total_cash(ones, fives, tens, twenties, fifties, hundreds))
