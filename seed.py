from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Pokemon, Stat, Move

engine = create_engine('sqlite:///pokemon.db')
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

charizard = Pokemon(name='Charizard', type='Fire')
charizard.moves = [Move(name='Flamethrower'), Move(name='Fly'), Move(name='Blast Burn'), Move(name='Fire Punch')]
charizard.stats = [Stat(name='ATTACK', value=12), Stat(name='DEFENSE', value=8)]

session.add(charizard)
session.commit()
