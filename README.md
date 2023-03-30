# Pokemon CLI Battle

Day after day, we walk the streets of New York City and hear the cries of the people. They beg for the same opportunity, and yet, their needs are ignored, leaving them to continue a meaningless existence.  We heard the call and decided that we would not all such an injustice to continue. 

EVERY HUMAN BEING DESERVES EQUAL ACCESS TO A CLI POKEMON BATTLE SIMULATOR.  EVERY. SINGLE. ONE.



## Description and Directions

In Pokemon CLI Battle, users will begin by creating a pokemon trainer ID and receiving $5000 to bet in battles.  After the trainer ID has been assigned, the player will begin a turn-based match against the computer with randomized Pokemon.  

Every Pokemon has the following: 
* Type (fire, water, grass)
* Skillset (4 unique moves assigned to the Pokemon)
* Stats (attack and defense)
* Health (20 bars that the Pokemon will lose depening on the attack used)

The user will be the first to attack in each match.  To begin, the user will select an attack assigned to either 1, 2, 3, or 4.  Once a Pokemon has been attacked its health bar counter will decrease.  The amount of bars lost will depend on the stats of the attack and defense from each Pokemon.  After the user's turn turn is over the computer will select an attack and the user's pokemon will lose health bars. 

Users will have an advantage or disadvantage in each battle depeneding on the type of their pokemon and attacks.  

Type advantages are as follows: 
* Fire is STRONG against Grass       
* Grass is STRONG against Water
* Water is STRONG against Fire

If the attack being used is STRONG against the type of the opponent's Pokemon the move will receive the following label: "It's super effective!"  This means that the attack stat will be HIGHER THAN NORMAL and REMOVE MORE HEALTH BARS from the Pokemon being attacked.  

FOR EXAMPLE: If Charmander (fire type) uses ember on Cyndiquil (fire type), the attack stat will be normal.  If Charmader (fire type) uses ember on Bulbasaur (grass type), the attack stat will be higer and remove more health bars.

Type disadvantages are as follows: 
* Fire is WEAK against Water
* Grass is WEAK against Fire
* Water is WEAK against Grass

If the attack being used is WEAK against the type of opponent's Pokemon, the move will recieve the following label: "It's not very effective..." This means that the attack stat will be LOWER THAN NORMAL and REMOVE FEWER HEALTH BARS from the Pokemon being attacked.

FOR EXAMPLE: If Charmander (fire type) uses ember on Cyndiquil (fire type), the attack stat will be normal.  If Charmader (fire type) uses ember on Squirtle (water type), the attack stat will be lower and do remove fewer health bars.


The match will end once the user or computer's health bars reach 0.  If the user wins, the computer will pay the user $500 and the user's account balance will increase.  If the computer wins, the user will pay the computer $500 dollars and the user's account balance will decrease.






## Getting Started

### Installing

1) Go to the Github Repo: https://github.com/russel64/Phase-3-Project/blob/main/pokemon.py
2) Clone the Repo onto your computer by clicking the green code button and copying the SSH link into your terminal
3) CD into the clone that was just created
4) Enter the following into the terminal to open the game:
```
code .
```

### Executing program

1) In VS Code, open a new terminal enter the following:
```
pipenv install
```

2) Enter the following into the terminal:
```
python pokemon.py
```

3) Follow the prompts on the screen and enjoy the game! 


## Help

If at any point the game behaves in an unusual manner, exit the game pressing "control + d" on your keyboard.  If you would like to try again, start the game again with: 
```
python pokemon.py
```

## Authors

Chris Chan 

Minyoung Shin

Bill Russell 

## Version History


* 0.1
    * Initial Release
    * Best Version
