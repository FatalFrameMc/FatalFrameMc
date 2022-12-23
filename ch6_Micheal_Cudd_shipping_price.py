# Micheal Cudd
# Module 06 Programming Assignment
# Part B
# This program calculates shipping costs.

# Create a program called shipping_price.py that calculates the shipping price for a purchase.
# Use a prompt to get (from the user) the number of items and the total weight of the package (in pounds).
# Then pass that data to a user-defined function that accepts both values as parameters and returns (not outputs)
# a shipping price based on the following guidelines:
#
#     Less than 3 items and less than one pound: $5.00 shipping charge.
#     Less than 3 items and one pound or over: $7.50 shipping charge.
#     3 to 5 items and less than two pounds: $8.50 shipping charge.
#     Anything else: $10.00 shipping charge.
#
# Display this returned value for the user.

num_items = int(input("How many Items? "))
weight = float(input("Weight in pounds? "))


def shipping_price(num_items, weight):

    # Less than 3 items and less than one pound: $5.00 shipping charge.
    if num_items < 3 and weight < 1:
        return "$5.00 shipping charge."

    # Less than 3 items and one pound or over: $7.50 shipping charge.
    if num_items < 3 and weight >= 1:
        return "$7.50 shipping charge"

    # 3 to 5 items and less than two pounds: $8.50 shipping charge.
    if (3 <= num_items <= 5) and weight <= 2:
        return "$8.50 shipping charge."

    # Anything else: $10.00 shipping charge.
    if num_items > 5 and weight >= 0:
        return "$10.00 shipping charge."


print(shipping_price(num_items, weight))
