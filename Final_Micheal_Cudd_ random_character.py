# Micheal Cudd
# Final
# This program creates a basic random character for DND 5e -

# all of
# a function that accepts at least one argument  <-- Random Character
# a function that returns a value (which can be same function as above)  <-- Random Character
# uses a loop in a meaningful way  <-- dice roller
# basic exception handling using try and except  <-- dice roller
#
# and at least one of the following, each in a meaningful way:
# uses a class
# uses a list or dictionary <-- Random Character
# reads / writes to files <-- working on for Random Character
###################################################################

import random


# Produce Character Stats
def character_stats():
    return random.randint(3, 18)


def skills_point():
    return random.randint(1, 5)


def character_skills():
    return random.choice(skill)


strength = character_stats()
dexterity = character_stats()
constitution = character_stats()
intelligence = character_stats()
wisdom = character_stats()
charisma = character_stats()


# Character Info
names = ['Amaltheia', 'Aranrhod', 'An Evandrus', 'Glaukos', 'Alexander',
         'Conchobar', 'Asklepios', 'Fenrir', 'Artemis', 'Giano', 'Chloe',
         'Kara', 'Meadhbh', 'Penelope', 'Pleione', 'Seppo', 'Takhma', 'Urupi',
         'Fionnuala', 'Marduk', 'Philander', 'Uror', 'Cernunnos', 'Mokosh',
         'Enyo', 'Calypso', 'Castiel', 'Arjuna', 'Junon', 'Johonaa', 'Maponos',
         'Yemaya',  'Suibne', 'Hormizd', 'Iphigenia', 'Endymion', 'Maia', 'Daire',
         'Connla', 'Nokomis', 'Tezcatlipoca', 'Pyrrhus', 'Philomele', 'Eris',
         'Bhumi', 'Dinesha',  'Angharad', 'Jarl', 'Kratos', 'Cleena']

race = ['Human', 'Dwarf', 'Elf', 'Halfling', 'Dragonborn', 'Gnome', 'Half-Elf',
        'Half-Orc', 'Goblin', 'Kobold', 'Shifter', 'Waforged']

classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin',
           'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']

language = ['Common', 'Draconic', 'Dwarven', 'Elvish', 'Halfling', 'Gnomish',
            'Orcish', 'Abyssal', 'Infernal', 'Giant', 'Goblin', 'Celestial',
            'Primordial', 'Sylvan', 'Undercommon']

alignment = ['Lawful Good', 'Lawful Neutral', 'Lawful Evil',
             'Neutral Good', 'Neutral', 'Neutral Evil',
             'Chaotic Good', 'Chaotic Neutral', 'Chaotic Evil']

background = ['Acolyte', 'Anthropologist', 'Archaeologist', 'Athlete', 'Charlatan',
              'City Watch', 'Criminal', 'Entertainer', 'Folk Hero', 'Gambler', 'Gladiator',
              'Hermit', 'Knight', 'Noble', 'Pirate', 'Sage', 'Shipwright', 'Smuggler', 'Soldier']

weapons = ['Short Sword', 'Long Sword', 'Mace', 'Staff', 'Dagger', 'Short Bow', 'Long Bow', 'Cross Bow',
           'Darts', 'Slings', 'Hammer', 'Battle Axe', 'Spear']

spells = ['Please choose the appropriate spells for the class and your campaign.']

armor = ['No-Armor', 'Plate', 'Padded', 'Leather', 'Studded Leather', 'Hide', 'Chain Mail',
         'Scale Mail', 'Breastplate', 'Half Plate', 'Ring Mail', 'Splint']

shield = ['No Shield', 'Shield']

skill = ['Acrobatics', 'Animal Handling', 'Arcana', 'Athletics', 'Deception', 'History', 'Insight',
         'Intimidation', 'Investigation', 'Medicine', 'Nature', 'Perception', 'Performance', 'Persuasion',
         'Religion', 'Slight of Hand', 'Stealth', 'Survival']

money = ['gp', 'sp', 'cp']


# Show Character on screen.
print(f'Name: {random.choice(names)}', end=' '*5)
print(f'Race: {random.choice(race)}', end=' '*5)
print(f'Class: {random.choice(classes)}')
print(f'Alignment: {random.choice(alignment)}', end=' '*5)
print(f'Background: {random.choice(background)}')
print('')
print(f'{"Strength:":13} {strength:>3}')
print(f'{"Dexterity:":13} {dexterity:>3}')
print(f'{"Constitution:":13} {constitution:>3}')
print(f'{"Intelligence:":13} {intelligence:>3}')
print(f'{"Wisdom:":13} {wisdom:>3}')
print(f'{"Charisma:":13} {charisma:>3}')
print('')
print(f'{"Armor:":11} {random.choice(armor)}')
print(f'{"Shield:":11} {random.choice(shield)}')
print(f'{"Weapon:":11} {random.choice(weapons)}')
print(f'{"Spells:":11} {random.choice(spells)}')
print(f'{"Languages:":11} {random.choices(language, k=2)}')
print(f'{"Skills:":11}', end=' ')
for i in range(5):
    print(character_skills(), skills_point(), end=', ')
print('')
print(f'{"Money:":11}', random.randint(1, 15), end=' ')
print(random.choice(money))
