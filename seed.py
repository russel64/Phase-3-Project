from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Pokemon, Stat, Move

engine = create_engine('sqlite:///pokemon.db')
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

session.query(Pokemon).delete()
session.query(Move).delete()
session.query(Stat).delete()

charizard = Pokemon(name='Charizard', type='Fire')
charizard.moves = [Move(name='Flamethrower'), Move(name='Fly'), Move(name='Blast Burn'), Move(name='Fire Punch')]
charizard.stats = [Stat(name='ATTACK', value=12), Stat(name='DEFENSE', value=8)]

new_pokemon = Pokemon(name='Pikachu', type='Electric')
new_pokemon.moves = [Move(name='Thunderbolt'), Move(name='Quick Attack'), Move(name='Iron Tail'), Move(name='Volt Tackle')]
new_pokemon.stats = [Stat(name='ATTACK', value=6), Stat(name='DEFENSE', value=5)]


session.add(new_pokemon)
session.add(charizard)
session.commit()
