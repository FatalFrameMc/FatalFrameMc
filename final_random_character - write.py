# Micheal Cudd
# Final
# This program creates a basic random character for DND 5e - and writes out the file

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


def character_stats():
    return random.randint(3, 18)


def skills():
    return random.choice(skill)


def skill_points():
    return random.randint(1, 5)


def languages():
    return random.choices(language, k=3)


# Character Info
names = ['Amaltheia', 'Aranrhod', 'An Evandrus', 'Glaukos', 'Alexander',
         'Conchobar', 'Asklepios', 'Fenrir', 'Artemis', 'Giano', 'Chloe',
         'Kara', 'Meadhbh', 'Penelope', 'Pleione', 'Seppo', 'Takhma', 'Urupi',
         'Fionnuala', 'Marduk', 'Philander', 'Uror', 'Cernunnos', 'Mokosh',
         'Enyo', 'Calypso', 'Castiel', 'Arjuna', 'Junon', 'Johonaa', 'Maponos', 'Yemaya',
         'Suibne', 'Hormizd', 'Iphigenia', 'Endymion', 'Maia', 'Daire', 'Connla', 'Nokomis',
         'Tezcatlipoca', 'Pyrrhus', 'Philomele', 'Eris', 'Bhumi', 'Dinesha',
         'Angharad', 'Jarl', 'Kratos', 'Cleena']

race = ['Human', 'Dwarf', 'Elf', 'Halfling', 'Dragonborn', 'Gnome', 'Half-Elf',
        'Half-Orc', 'Tiefling', 'Leonin', 'Satyr', 'Owlin', 'Aarakocra', 'Aasimar',
        'Bugbear', 'Changling', 'Goblin', 'Harengon', 'Kenku', 'Kobold', 'Shifter',
        'Tabazi', 'Tortle',  'Waforged']

classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger',
           'Rogue', 'Sorcerer', 'Warlock', 'Wizard', 'Artificer', 'Blood Hunter']

language = ['Common', 'Draconic', 'Dwarven', 'Elvish', 'Halfling', 'Gnomish', 'Orcish', 'Abyssal',
            'Infernal', 'Giant', 'Goblin', 'Celestial', 'Primordial', 'Sylvan', 'Undercommon']

alignment = ['Lawful Good', 'Lawful Neutral', 'Lawful Evil',
             'Neutral Good', 'Neutral', 'Neutral Evil',
             'Chaotic Good', 'Chaotic Neutral', 'Chaotic Evil']

background = ['Acolyte', 'Anthropologist', 'Archaeologist', 'Astral Drifter', 'Athlete', 'Charlatan',
              'City Watch', 'Criminal', 'Entertainer', 'Faceless', 'Folk Hero', 'Gambler', 'Gladiator',
              'Hermit', 'Knight', 'Noble', 'Pirate', 'Sage', 'Shipwright', 'Smuggler', 'Soldier', 'Urchin']

weapons = ['Please choose the appropriate weapon for your campaign.']

spells = ['Please choose the appropriate spells for the class and your campaign.']

armor = ['No-Armor', 'Plate', 'Padded', 'Leather', 'Studded Leather', 'Hide', 'Chain Mail',
         'Scale Mail', 'Breastplate', 'Half Plate', 'Ring Mail', 'Splint']

skill = ('Acrobatics', 'Animal Handling', 'Arcana', 'Athletics', 'Deception', 'History', 'Insight',
         'Intimidation', 'Investigation', 'Medicine', 'Nature', 'Perception', 'Performance', 'Persuasion',
         'Religion', 'Slight of Hand', 'Stealth', 'Survival')


strength = character_stats()
dexterity = character_stats()
constitution = character_stats()
intelligence = character_stats()
wisdom = character_stats()
charisma = character_stats()
languages_r = languages()


f = open('random_character.txt', 'w')
f.write(f'Name: {random.choice(names)}' + '     ')
f.write(f'Race: {random.choice(race)}' + '     ')
f.write(f'Class: {random.choice(classes)}' + '     ')
f.write('\n')
f.write(f'Alignment: {random.choice(alignment)}' + '     ')
f.write(f'Background: {random.choice(background)}')
f.write('\n')
f.write('\n')
f.write(f'{"Strength:":13} {strength:>3}')
f.write('\n')
f.write(f'{"Dexterity:":13} {dexterity:>3}')
f.write('\n')
f.write(f'{"Constitution:":13} {constitution:>3}')
f.write('\n')
f.write(f'{"Intelligence:":13} {intelligence:>3}')
f.write('\n')
f.write(f'{"Wisdom:":13} {wisdom:>3}')
f.write('\n')
f.write(f'{"Charisma:":13} {charisma:>3}')
f.write('\n')
f.write(f'Armor: {random.choice(armor)}')
f.write('\n')
f.write('\n')
f.write(random.choice(weapons))
f.write('\n')
f.write(random.choice(spells))
f.write('\n')
f.write(f'Languages: {str(languages_r)}')
f.write('\n')
f.write('Skills: ')
for i in range(5):
    f.write(str(skills()) + ' ' + str(skill_points()) + ' ')

f.close()

with open('random_character.txt', 'r') as r:
    contents = r.read()

print(contents)
