#!/usr/bin/python3
"""
Contains the class definition of a City
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    City class that links to the MySQL table cities
    
    Attributes:
        id: auto-generated unique integer, primary key, can't be null
        name: string with maximum 128 characters, can't be null
        state_id: integer, foreign key to states.id, can't be null
    """
    __tablename__ = 'cities'
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

