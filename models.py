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