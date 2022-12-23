import random


class Character:
    def __init__(self):
        self.name = name
        self.role = role
        self.race = race
        self.alignment = alignment
        self.background = background

    def name(self):
        return random.choice(name)

    def role(self):
        return random.choice(role)

    def race(self):
        return random.choice(race)

    def alignment(self):
        return random.choice(alignment)

    def background(self):
        return random.choice(background)

class Fighter(Character):
    def __init__(self):
        Character.__init__(self)
        self.armor = armor
        self.shield = shield
        self.weapon = martial_weapon

    def armor(self):
        return random.choice(armor)

    def shield(self):
        return random.choice(shield)

    def weapon(self):
        return random.choice(martial_weapon)


class Wizard(Character):
    def __init__(self):
        Character.__init__(self)
        self.armor = c_armor
        self.shield = shield
        self.weapon = c_weapon

    def armor(self):
        return random.choice(c_armor)

    def shield(self):
        return random.choice(shield)

    def weapon(self):
        return random.choice(c_weapon)

name = ['Amaltheia', 'Aranrhod', 'An Evandrus', 'Glaukos', 'Alexander',
         'Conchobar', 'Asklepios', 'Fenrir', 'Artemis', 'Giano', 'Chloe',
         'Kara', 'Meadhbh', 'Penelope', 'Pleione', 'Seppo', 'Takhma', 'Urupi',
         'Fionnuala', 'Marduk', 'Philander', 'Uror', 'Cernunnos', 'Mokosh',
         'Enyo', 'Calypso', 'Castiel', 'Arjuna', 'Junon', 'Johonaa', 'Maponos',
         'Yemaya',  'Suibne', 'Hormizd', 'Iphigenia', 'Endymion', 'Maia', 'Daire',
         'Connla', 'Nokomis', 'Tezcatlipoca', 'Pyrrhus', 'Philomele', 'Eris',
         'Bhumi', 'Dinesha',  'Angharad', 'Jarl', 'Kratos', 'Cleena']

race = ['Human', 'Dwarf', 'Elf', 'Halfling', 'Dragonborn', 'Gnome', 'Half-Elf',
        'Half-Orc', 'Goblin', 'Kobold', 'Shifter', 'Waforged']

role = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin',
        'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']



alignment = ['Lawful Good', 'Lawful Neutral', 'Lawful Evil',
             'Neutral Good', 'Neutral', 'Neutral Evil',
             'Chaotic Good', 'Chaotic Neutral', 'Chaotic Evil']

background = ['Acolyte', 'Anthropologist', 'Archaeologist', 'Athlete', 'Charlatan',
              'City Watch', 'Criminal', 'Entertainer', 'Folk Hero', 'Gambler', 'Gladiator',
              'Hermit', 'Knight', 'Noble', 'Pirate', 'Sage', 'Shipwright', 'Smuggler', 'Soldier']

martial_weapon = ['Short Sword', 'Long Sword', 'Mace', 'Staff', 'Dagger', 'Short Bow', 'Long Bow',
                  'Cross Bow', 'Darts', 'Slings', 'Hammer', 'Battle Axe', 'Spear']

c_weapon = ['Staff', 'Dagger','Cross Bow', 'Darts', 'Slings']

armor = ['No-Armor', 'Plate', 'Padded', 'Leather', 'Studded Leather', 'Hide', 'Chain Mail',
         'Scale Mail', 'Breastplate', 'Half Plate', 'Ring Mail', 'Splint']

c_armor = ['No-Armor', 'Robe +1' 'Mage Armor']

shield = ['No Shield', 'Shield']

