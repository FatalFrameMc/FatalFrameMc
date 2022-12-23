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



if what_letter is not what_letter.islower():
	return what_letter.lower()
if first_word is not first_word.islower():
	return first_word.lower()
if second_word is not second_word.islower():
	return second_word.lower()
if third_word is not third_word.islower():
	return third_word.lower()

total = word1_search(first_word).count(letter_search(what_letter)) + word2_search(second_word).count(letter_search(what_letter)) + word3_search(third_word).count(letter_search(what_letter))
# format to directions. but working.
print('-' * 35)
print(f'{first_word:20} {what_letter:^5} {word1_search(first_word).count(letter_search(what_letter)):^5}')
print(f'{second_word:20} {what_letter:^5} {word2_search(second_word).count(letter_search(what_letter)):^5}')
print(f'{third_word:20} {what_letter:^5} {word3_search(third_word).count(letter_search(what_letter)):^5}')
print('-' * 35)