# Micheal Cudd
# Module 09 Programming Assignment
# Part

# This program uses a class for a shopping cart checkout

# (1) Create the ItemToPurchase class with the following specifications:
#     Attributes
#         item_name (string)
#         item_price (float)
#         item_quantity (int)
#     Default constructor
#         Initializes item's name = "none", item's price = 0, item's quantity = 0
#     Method
#         print_item_cost()
#
# (2) In the main section of your code (not in the class definition),
#     prompt the user for two items and create two objects of the ItemToPurchase class.
#
# (3)
#     Add the costs of the two items together and output the total cost.

# class ItemToPurchase set up
class ItemToPurchase:
    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0.0
        self.item_quantity = 0

# def print_item_cost() - Help from Tracy
# method(which is really a function) to calculate a total and  return (not print)
# the value, then you
# could:
# item1.print_item_cost() + item2.print_item_cost()


    def print_item_cost(self):
        print(self.item_name, self.item_quantity, '@', self.item_price, '=', (self.item_price * self.item_quantity))

    def print_item_cost2(self):
        return self.item_price * self.item_quantity



# item 1
item1 = ItemToPurchase()
item1.item_name = input("Item Name? ")
item1.item_price = float(input("Price? "))
item1.item_quantity = int(input("Quantity? "))
# item1.print_item_cost()

# item 2
item2 = ItemToPurchase()
item2.item_name = input("Item Name? ")
item2.item_price = float(input("Price? "))
item2.item_quantity = int(input("Quantity? "))
# item2.print_item_cost()

# total cost of the items
# TOTAL COST
# Chocolate Chips 1 @ $3.5 = $3.5
# Bottled Water 10 @ $1.25 = $12.5
#
# Total: $15.5
print('Total COST:')
item1.print_item_cost()
item2.print_item_cost()
print('Total: ', end = ' ')
print(item1.print_item_cost2() + item2.print_item_cost2())
