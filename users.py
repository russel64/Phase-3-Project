from sqlalchemy import create_engine, func
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
import random
# IMPORT USER TO USE CLASS
from models import User, Base


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///Pokemon.db")
Base.metadata.create_all(bind = engine)
Base = declarative_base
Session = sessionmaker(bind=engine)
session = Session()

trainer_num_list = []

 # register a new user:
def register():
    new_num = random.randint(1001, 9999)
    if new_num not in trainer_num_list:
        trainer_num_list.append(new_num)
        User(new_num)
        print(f"Your TRAINER ID is {new_num}")
        # SEND TO THEIR ACCOUNT = show trainer id and their balance 
    else:
        register()


def login(num):
    info = session.query(User).filter(User.trainer_number == num).all()
    account(info)

def account(info):
    print(info)
    # show tirainer id and their balance 
    # START BATTLE PROMPT - .fight function 
    pass

print("\n")
trainer_num = str(input('PLEASE LOGIN USING YOUR TRAINER ID ( If you wish to register, please enter "r" ): '))

if trainer_num == 'r':
    register()
else:
    num = int(trainer_num)
    login(num)




# after loggin, trainer can now choose to fight pokemon
# update currency after each battle
# keep program running until we quit

    

    
