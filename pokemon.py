from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models import User, Base, Pokemon, Stat, Move

import time
import numpy as np
import sys
import random

engine = create_engine("sqlite:///pokemon.db")
Session = sessionmaker(bind=engine)
session = Session()

# register a new user:
def register():
    new_num = random.randint(1001, 9999)
    counter = session.query(User).filter(User.trainer_number == new_num).count()
    if counter != 1:
        user = User(new_num)
        session.add(user)
        session.commit()
        print("Welcome to the world of Pokemon!")
        print('''

                                  ,'\                                   
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|
                                
                                                                                    ''')
        print("\n")
        print(f"Your TRAINER ID is {new_num}")
        print("\n")
        account(user)
    else:
        register()

def login(num): 
    counter = session.query(User).filter(User.trainer_number == num).count()
    if counter == 1:
        print(f"~ Welcome back Trainer #{num}! ~")
        print("\n")
        user = session.query(User).filter(User.trainer_number == num).all()
        account(user)
    else:
        print("Trainer ID does not exist. Please try again")
        init()


# Delay printing
def delay_print(s):
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


def pokemon():
    poke = (session.query(Pokemon)[random.randint(0,21)])
    stats = (session.query(Stat).filter(Stat.pokemon_id == poke.id).all())
    moves = (session.query(Move).filter(Move.pokemon_id == poke.id).all())
    poke_dict = {
        "Name": poke.name,
        "Type": poke.type,
        "Attack": stats[0].value,
        "Defense": stats[1].value,
        "Moves": [move.name for move in moves],
        "Bars" : 10,
        "Health" : '==================='
    }
    return poke_dict

    
def fight(pokemon1, pokemon2):

    print("-----POKEMON BATTLE-----")
    delay_print("\nYOUR POKEMON:")
    print(f"\n{pokemon1['Name']}")
    print(f"TYPE: {pokemon1['Type']}")
    print(f"ATTACK: {pokemon1['Attack']}")
    print(f"DEFENSE: {pokemon1['Defense']}")
    print("LVL", int(3*((pokemon1['Attack'] + pokemon1['Defense'])/2)))
    print("\nVS")
    delay_print("\nOPPONENT'S POKEMON:")
    print(f"\n{pokemon2['Name']}")
    print(f"TYPE: {pokemon2['Type']}")
    print(f"ATTACK: {pokemon2['Attack']}")
    print(f"DEFENSE: {pokemon2['Defense']}")
    print("LVL", int(3*((pokemon2['Attack'] + pokemon2['Defense'])/2)))

    time.sleep(2)

    # Type advantages
    version = ['Fire', 'Water', 'Grass']
    for i,k in enumerate(version):
        if pokemon1['Type'] == k:
            # Both are same type
            if pokemon2['Type'] == k:
                string_1_attack = '\nIts not very effective...'
                string_2_attack = '\nIts not very effective...'

            # pokemon2 is STRONG
            if pokemon2['Type'] == version[(i+1)%3]:
                pokemon2['Attack'] *= 2
                pokemon2['Defense'] *= 2
                pokemon1['Attack'] /= 2
                pokemon1['Defense'] /= 2
                string_1_attack = '\nIts not very effective...'
                string_2_attack = '\nIts super effective!'

            # pokemon2 is WEAK
            if pokemon2['Type'] == version[(i+2)%3]:
                pokemon1['Attack'] *= 2
                pokemon1['Defense'] *= 2
                pokemon2['Attack'] /= 2
                pokemon2['Defense'] /= 2
                string_1_attack = '\nIts super effective!'
                string_2_attack = '\nIts not very effective...'


    # Now for the actual fighting...
    # Continue while pokemon still have health
    while (pokemon1['Bars'] > 0) and (pokemon2['Bars'] > 0):
        # Print the health of each pokemon
        print(f"\n{pokemon1['Name']}\t\tHLTH\t{pokemon1['Health']}")
        print(f"{pokemon2['Name']}\t\tHLTH\t{pokemon2['Health']}\n")

        print(f"Go {pokemon1['Name']}!")
        for i, x in enumerate(pokemon1['Moves']):
            print(f"{i+1}.", x)
        index = int(input('Pick a move: '))
        while index > 4:
            print("Please pick either 1, 2, 3, or 4")
            index = int(input('Pick a move: '))
        delay_print(f"\n{pokemon1['Name']} used {pokemon1['Moves'][index-1]}!")
        time.sleep(1)
        delay_print(string_1_attack)

        # Determine damage
        pokemon2['Bars'] -= pokemon1['Attack']
        pokemon2['Health'] = ""

        money = np.random.choice(500)
        if pokemon2['Bars'] <= 0: 
            delay_print("\n..." + pokemon2['Name'] + ' fainted.')
            delay_print(f"\nOpponent paid you ${money}.\n")
            break

        # Add back bars plus defense boost
        for j in range(int(pokemon2['Bars']+.1*pokemon2['Defense'])):
            pokemon2['Health'] += "="

        time.sleep(1)
        print(f"\n{pokemon1['Name']}\t\tHLTH\t{pokemon1['Health']}")
        print(f"{pokemon2['Name']}\t\tHLTH\t{pokemon2['Health']}\n")
        time.sleep(.5)

        # Check to see if Pokemon fainted
       

        # Pokemon2s turn
        print(f"Go {pokemon2['Name']}!")
        for i, x in enumerate(pokemon2['Moves']):
            print(f"{i+1}.", x)
        rand = random.randint(1,4)
        index = int(rand)
        delay_print(f"\n{pokemon2['Name']} used {pokemon2['Moves'][index-1]}!")
        time.sleep(1)
        delay_print(string_2_attack)

        # Determine damage
        pokemon1['Bars'] -= pokemon2['Attack']
        pokemon1['Health'] = ""

        money = np.random.choice(500)
        if pokemon1['Bars'] <= 0:
            delay_print("\n..." + pokemon1['Name'] + ' fainted.')
            delay_print(f"\nYou paid opponent ${money}.\n")
            break

        # Add back bars plus defense boost
        for j in range(int(pokemon1['Bars']+.1*pokemon1['Defense'])):
            pokemon1['Health'] += "="

        time.sleep(1)
        print(f"{pokemon1['Name']}\t\tHLTH\t{pokemon1['Health']}")
        print(f"{pokemon2['Name']}\t\tHLTH\t{pokemon2['Health']}\n")
        time.sleep(.5)

        # Check to see if Pokemon fainted
        

        
        

        
    check = input("Would you like to battle again? Enter y to continue or press any other button to exit:")
    if check.lower() == "y":
        print("Prepare for next challenger!")
        fight(pokemon(), pokemon())
    else:
        print("Thanks for playing!")
        exit()

# START OF PROGRAM:
def init():
    print("\n")
    trainer_num = str(input('PLEASE LOGIN USING YOUR TRAINER ID ( If you wish to register, please enter "r" ): '))
    print("\n")
    if trainer_num == 'r':
        register()
    else:
        num = int(trainer_num)
        login(num)

def account(user):
    print(user)
    print("\n")

    # START BATTLE PROMPT:
    check = input("To start a battle, enter 's' to start:")
    if check.lower() == "s":
        print("Preparing the next challenger!")
        print(Pokemon.all)
        # PELASE FIX AGTER CHRIS IS DONE (-:
        fight(pokemon(), pokemon())
    else:
        print("\n")
        print("Thanks for visiting!")
        print("\n")
        exit()

init()






  