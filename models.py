from sqlalchemy import ForeignKey, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Pokemon(Base):
    __tablename__ = "Pokemon"

    id = Column("key", Integer, primary_key = True)
    category = Column("category", String)