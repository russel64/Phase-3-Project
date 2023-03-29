from models import Base, Pokemon, Moveset
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine("sqlite:///Pokemon.db")
Base.metadata.create_all(bind = engine)
Base = declarative_base

Session = sessionmaker(bind=engine)
session = Session()

session.query(Pokemon).delete()
session.query(Moveset).delete()

p1 = Pokemon("Charizard")
p2 = Pokemon("Blastoise")
p3 = Pokemon("Venusaur")
p4 = Pokemon("Billysaur")

m1 = Moveset("FlameThrower")

session.add_all([m1])
session.add_all([p1, p2, p3])
session.commit()