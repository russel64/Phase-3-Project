from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()



class Move(Base):
    __tablename__ = 'move'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    pokemon_id = Column(Integer, ForeignKey('pokemon.id'))
    pokemon = relationship('Pokemon', back_populates='moves')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"(Name: {self.name},)"


class Stat(Base):
    __tablename__ = 'stat'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(Integer)
    pokemon_id = Column(Integer, ForeignKey('pokemon.id'))
    pokemon = relationship('Pokemon', back_populates='stats')

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"(Name: {self.name}, Value: {self.value})"


class Pokemon(Base):
    all = []
    __tablename__ = 'pokemon'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    moves = relationship('Move', back_populates='pokemon')
    stats = relationship('Stat', back_populates='pokemon')

    def __init__(self, name, type):
        self.name = name
        self.type = type
        
        Pokemon.all.append(self) 

    def __repr__(self):
        return f"(Name: {self.name}, Type: {self.type})"      

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
        return f"(TRAINER ID: {self.trainer_number}, BALANCE: {self.money})"
    