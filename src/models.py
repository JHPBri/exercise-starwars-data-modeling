import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable = False)
    Password = Column (String(50), nullable = False)

class Search(Base):
    __tablename__ = 'Search'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    search = Column(String(250))
    User_id = Column(Integer, ForeignKey('User.id'))
    Characters_id = Column(Integer, ForeignKey('Characters.id'))
    Vehicles_id = Column(Integer, ForeignKey('Vehicles.id'))
    Planets_id = Column(Integer, ForeignKey('Planets.id'))
    User = relationship(User)


class Characters(Base):
    __tablename__ = 'Characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    height = Column(Integer)
    hair_color = Column(String(50))
    skin_color = Column(String(50))
    birth_year = Column(Integer)
    gender = Column(String(50))
    home_world = Column(String(50))
    favorite = Column(String(250))
    Search = relationship(Search)

class Vehicles(Base):
    __tablename__ = 'Vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    model = Column(String(50))
    manufacturer = Column(String(50))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    max_atmosphereing_speed = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String(50))
    vehicle_class = Column(String(50))
    Search = relationship(Search)

class Planets(Base):
    __tablename__ = 'Planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    diameter = Column(Integer)
    climate = Column(String(50))
    gravity = Column(String(50))
    terrain = Column(String(50))
    surface_water = Column(String(50))
    population = Column(Integer)
    Search = relationship(Search)

class Favorite(Base):
    __tablename__ = 'Favorite'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    Characters_favorite = Column(String(50),ForeignKey('Characters.favorite'))
    Vehicles_favorite = Column(String(50),ForeignKey('Vehicles.favorite'))
    Planets_favorite = Column(String(50),ForeignKey('Planets.favorite'))
    User_id = Column(Integer, ForeignKey('User.id'))
    User = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')