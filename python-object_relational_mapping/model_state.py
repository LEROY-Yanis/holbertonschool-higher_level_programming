#!/usr/bin/python3
"""
Contains the class definition of a State and an instance Base
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class that links to the MySQL table states
    
    Attributes:
        id: auto-generated unique integer, primary key, can't be null
        name: string with maximum 128 characters, can't be null
    """
    __tablename__ = 'states'
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)