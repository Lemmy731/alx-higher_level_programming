#!/usr/bin/python3
""" file that contains the class definition of a State"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetatdata = MetaData()
Base = declarative_base(metadata = mymetadata)

class State(Base):
    """ state base"""
    
    __tablename__ = 'states'
    id = Column(Integer, Unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    
