#!/usr/bin/python3                                                                                                                         
""" file that contains the class definition of a city"""

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

class City(Base):
    """ city Base"""
    __tablename__ = 'cities'
    id = Column(Integer, Unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
