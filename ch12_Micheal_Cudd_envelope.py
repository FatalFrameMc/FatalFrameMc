# Micheal Cudd
# Module 12 Programming Assignment
# Part B
# This program creates a mock envelope.


# Create a program called envelope.py that prompts the user to input the following,
# storing each in a separate variable:
#
#     Recipient's name
#     Address
#     City
#     State
#     Zip Code
#
# Then, the program should create a new file called envelope.txt with a rudimentary mailing envelope:
#     Your name and return address at the top-left followed by the recipient's name and address.

#recipient input
name = input('What is the recipients name? ').title()
address = input('What is their address? ').title()
city = input('What is the name of their city? ').title()
state = input('What is the name of their state? ').title()
zip_code = input('What is their zip code? ')

space = (' '*30)

r_address = [city, state, zip_code]
recipient_address = ' '.join(r_address)

# my information
f = open('envelope.txt', 'w+')
f.write('Micheal Cudd')
f.write('\n')
f.write('3000 N Dysart Rd')
f.write('\n')
f.write('Avondale, AZ 85392')
f.write('\n')
f.write('\n')

# write recipient input
f.write(space)
f.write(name)
f.write('\n')
f.write(space)
f.write(address)
f.write('\n')
f.write(space)
f.write(recipient_address)

f.close()

with open('envelope.txt', 'r') as r:
    contents = r.read()
print('\n')
print('\n')

print(contents)
