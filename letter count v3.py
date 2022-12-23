# Micheal Cudd
# Module 07 Programming Assignment
# Part A

# This program counts the number of certain letters in 3 inputs.

# Create a program in a file named letter_count.py. Prompt the user to enter three different words or phrases,
# one at a time; store each response in a separate variable.
# Next, prompt the user a letter they wish to count.
# Finally, count how many times the letter occurs in each of the three
# words/phrases, regardless of case (uppercase or lowercase),
# as well as the total; output a formatted table displaying the results.
# Be sure your program includes adequate directions for the user.
# Sample Program Run:
#
# Enter the first word: Apple
# Enter the first word: Pear
# Enter the first word: OrAnGe
# Enter the letter to count: p
# Occurrences of p
# ---------------------------------
# Apple                           2
# Pear                            1
# OrAnGe                          0
# ---------------------------------
# Total                           3

print("Please choose 3 words or phrases with a max of 16 characters including spaces.")
# user word/phrases.
first_word = input("What is your first word or phrase? ")
second_word = input("What is your second word or phrase? ")
third_word = input("What is your third word or phrase? ")

# what letter they want to search.
what_letter = input("What letter do you want to count? ")

fword = first_word.lower()
sword = second_word.lower()
tword = third_word.lower()

total = fword.count(what_letter) + sword.count(what_letter) + tword.count(what_letter)


print('-' * 35)
print(f'{first_word:20} {what_letter:^5} {fword.count(what_letter):^5}')
print(f'{second_word:20} {what_letter:^5} {sword.count(what_letter):^5}')
print(f'{third_word:20} {what_letter:^5} {tword.count(what_letter):^5}')
print('-' * 35)
print(f'{"Total":26} {total:^5}')