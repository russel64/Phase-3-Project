from models import Base, Pokemon
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine("sqlite:///Pokemon.db")
Base.metadata.create_all(bind = engine)
Base = declarative_base

Session = sessionmaker(bind=engine)
session = Session()

session.query(Pokemon).delete