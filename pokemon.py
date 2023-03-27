import time
import numpy as np
import sys

#Delay printing 

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

#Create the class

class Pokemon:
    def __init__(self, name, types, moves, EVs, health = '==================='):
        #save variable as attributes
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20 # Amount of health bars

def fight(self, Pokemon2):
    #Allow two pokemon to fight each other

    #print fight information
    print("----POKEMON BATTLE----")
    print(f"\n{self.name}")
    print("TYPE/", self.types)
    print("ATTACK/", self.attack)
    print("DEFENSE/", self.defense)
    print("LVL/", 3*(1+np.mean([self.attack, self.defense])))
    print("\nVS")
    print(f"\n{Pokemon2.name}")
    print("TYPE/", Pokemon2.types)
    print("ATTACK/", Pokemon2)
