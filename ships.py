"""ships.py
By Jesse Forgione
Generates a ship from a string.
"""

import random, string
import render2

# Get valid characters, randomizing their values
chars = list(string.printable[0:36])
random.shuffle(chars)
CHARS = ""

for i in chars:
    CHARS += i


class Ship(object):
    pattern = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    length = 5
    width = 2
    brand = 1

    accuracy = 0
    power = 0
    pconsume = 1
    speed = 1
    defense = 1
    shields = 0

    blocks = 2
    
    weapons = [0, 0, 0]
    armor = [0, 0, 0]
    engines = [0, 0, 0]
    misc = [0, 0, 0]

    BRANDS = ["Jeb's Junkers",
              "Parasol Corps.",
              "Melian Incorporated",
              "Grah-Zin Star Cruisers",
              "Veias Intelligency",
              "Bob's Bits and Pieces"]
    
    def __str__(self):
        s = render2.genMelianShape(self.blocks, [self.weapons, self.armor,
                                                 self.engines, self.misc],
                                   [sum(self.weapons), sum(self.armor),
                                    sum(self.engines), sum(self.misc)])
        #s = render2.drawShip(self)

        s += "\nBrand: " + self.BRANDS[self.brand]
        
        s += "\nWeapons: " + str(sum(self.weapons))
        s += "\n   Lasers: " + str(self.weapons[0])
        s += "\n   Railguns: " + str(self.weapons[1])
        s += "\n   MGs: " + str(self.weapons[2])

        s += "\n\nDefense: " + str(round(self.defense, 1))
        s += "\nShields: " + str(round(self.shields, 1))

        s += "\n\nAccuracy Bonus: +" + str(self.accuracy)
        
        s += "\n\nSpeed: " + str(self.speed)

        s += "\n\nPower: " + str(self.power)
        s += "\nConsumption: " + str(self.pconsume)
            
        return s

    def attack(self):
        """Gets the damage from a full round of attacking."""

        i = 0

        # More or less damage based on power
        powermult = self.power / self.pconsume

        lazdam = 0
        damage = 0
        
        for j in self.weapons:
            for k in range(j):
                if i == 0:
                    lazdam += 1 * random.randrange(3 + self.accuracy) * powermult
                elif i == 1:
                    damage += 3 * random.randrange(2 + self.accuracy) * powermult
                else:
                    damage += 2 * random.randrange(1 + self.accuracy)* powermult
                
            i += 1

        damage /= 2
        lazdam /= 2

        return damage, lazdam

    def defend(self, damage):
        damage, lazdam = damage

        damage -= self.speed / 2
        lazdam -= self.speed / 2

        if damage < 0:  damage = 0
        if lazdam < 0:  lazdam = 0

        if self.shields <= 0:
            lazdam += damage
        elif damage > self.shields:
            damage -= self.shields
            self.shields = 0
            lazdam += damage
        else:
            self.shields -= damage

        self.defense -= lazdam
        
        return lazdam
    
    def generate(self, pattern):
        """Generate the ship."""
        pattern = formatp(pattern)

        # Width
        wn = pattern[0] % 9
        if wn in range(0,3):    self.width = 1
        elif wn in range(3,6):  self.width = 2
        elif wn in range(6,8):  self.width = 3
        elif wn == 8:   self.width = 4
        else:   self.width = 5
        del wn

        # Length
        ln = pattern[1] % 18
        if ln == 0: self.length = 1
        elif ln == 1:   self.length = 2
        elif ln in range(2,4):  self.length = 3
        elif ln in range(4,8):  self.length = 4
        elif ln in range(8,12):  self.length = 5
        elif ln in range(12,15):  self.length = 6
        elif ln == 15:   self.length = 7
        elif ln == 16:   self.length = 8
        elif ln == 17:   self.length = 9
        del ln

        # Brand
        wn = pattern[2] % 9
        if wn in range(0,3):    self.brand = 1
        elif wn in range(3,6):  self.brand = 2
        elif wn in range(6,8):  self.brand = 3
        elif wn == 8:   self.brand = 4
        else:   self.brand = 5
        del wn

        # Power
        ln = pattern[3] % 18
        if ln == 0: self.power = 1
        elif ln == 1:   self.power = 2
        elif ln in range(2,4):  self.power = 3
        elif ln in range(4,8):  self.power = 4
        elif ln in range(8,12):  self.power = 5
        elif ln in range(12,15):  self.power = 6
        elif ln == 15:   self.power = 7
        elif ln == 16:   self.power = 8
        elif ln == 17:   self.power = 9
        del ln

        # Other stuff
        self.blocks = self.length * self.width

        total = sum(pattern[4:16])

        # Weapons
        wep = pattern[4:7]
        wept = round(sum(wep) * self.blocks / total)
        self.weapons = subtype(wept, wep)

        self.pconsume += self.weapons[0]
        self.pconsume += self.weapons[1] * 1.5
        self.pconsume += self.weapons[2] * 0.5

        # Armor
        arm = pattern[7:10]
        armt = round(sum(arm) * self.blocks / total)
        self.armor = subtype(armt, arm)

        self.defense += self.armor[0] * 2
        self.defense += self.armor[1] * 4
        self.defense += self.armor[2] * 6

        self.speed -= self.armor[0] * 0.5
        self.speed -= self.armor[1]
        self.speed -= self.armor[2] * 2

        # Engines
        eng = pattern[10:13]
        engt = round(sum(eng) * self.blocks / total)
        self.engines = subtype(engt, eng)

        self.speed += self.engines[0]
        self.speed += self.engines[1] * 2
        self.speed += self.engines[2] * 3

        self.pconsume += self.engines[0] * 0.5
        self.pconsume += self.engines[1]
        self.pconsume += self.engines[2] * 1.5

        # Misc
        mis = pattern[13:16]
        mist = round(sum(mis) * self.blocks / total)
        self.misc = subtype(mist, mis)

        self.accuracy += self.misc[0]
        self.pconsume += self.misc[0] * 0.5

        self.power += self.misc[1] * 2
        self.speed -= self.misc[1]

        self.shields += self.misc[2] * 2
        self.pconsume -= self.misc[2]

        # Cannot have speed of less than 1
        if self.speed < 1:  self.speed = 1

        # Set blocks in case of faulty rounding
        self.blocks = sum(self.weapons) + sum(self.armor) + \
                      sum(self.engines) + sum(self.misc)

        self.pattern = pattern

def formatp(pattern):
    """Format a string into the correct number of characters"""
    # Seed the randomness
    seed = ""
    for i in pattern.lower():
        if i in CHARS:
            seed += str(CHARS.index(i))
    
    random.seed(seed)

    pl = list(pattern) # Convert to list for easier editing

    #===========================================================
    ivc = []    # Get all Invalid characters
    for char in pl:
        if char not in CHARS:
            if char not in ivc:
                ivc.append(char)

    for char in ivc:    # Remove the invalid characters
        while char in pl:
            pl.remove(char)

    #============================================================
    if len(pl) < 16: # Add more characters
        for i in range(16 - len(pl)):  # Add random characters
            pl.append(random.choice(CHARS))
            
    elif len(pl) > 16: # Remove some characters
        for i in range(len(pl) - 16):  # Remove random characters
            pl.pop(random.randrange(0, len(pl)))

    #============================================================
    # Convert to list of numbers
    pattern = []
    for c in pl:
        pattern.append(CHARS.index(c))
            

    return pattern

def subtype(blocks, ratio):
    """Computes the blocks in a subtype"""
    t = sum(ratio)

    parts = []
    
    parts.append(round(blocks * ratio[0]/t))
    parts.append(round(blocks * ratio[1]/t))
    parts.append(round(blocks * ratio[2]/t))

    return parts

def possub(x, y):
    """Returns x - y, minimum 0."""

if __name__ == "__main__":
    ship = Ship()
    ship.generate(input("Ship Pattern: "))
    print()
    print(ship)
    input()
