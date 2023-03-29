from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Pokemon(Base):
    __tablename__ = 'pokemon'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    moves = relationship('Move', back_populates='pokemon')
    stats = relationship('Stat', back_populates='pokemon')

class Move(Base):
    __tablename__ = 'move'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    pokemon_id = Column(Integer, ForeignKey('pokemon.id'))
    pokemon = relationship('Pokemon', back_populates='moves')

class Stat(Base):
    __tablename__ = 'stat'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(Integer)
    pokemon_id = Column(Integer, ForeignKey('pokemon.id'))
    pokemon = relationship('Pokemon', back_populates='stats')

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
    