from sqlalchemy import ForeignKey, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Pokemon(Base):
    __tablename__ = "Pokemon"

    id = Column("key", Integer, primary_key = True)
    pokemon = Column("Pokemon", String)

    def __init__(self, pokemon):
        self.pokemon = pokemon

    def __repr__(self):
        return f"{self.id} {self.pokemon}"
    

class Moveset(Base):
    __tablename__ = "MoveSets"

    id = Column("key", Integer, primary_key = True)
    moveset = Column("MoveSet", String)

    def __init__(self, moveset):
        self.moveset = moveset

    def __repr__(self):
        return f"{self.id} {self.moveset}"
    
class User(Base):

    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    trainer_number = Column(Integer)
    money = Column(Integer)

    trainers = []
    def __init__(self, trainer_number):
        self.trainer_number = trainer_number
        self.money = 5000
        User.trainers.append(self)

    def __repr__(self):
        return f"(Trainer Number: {self.trainer_number}, Balance: {self.money})"
    