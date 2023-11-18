#!/usr/bin/python3

'''model_city.py'''
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from model_state import Base


class City(Base):
    '''Class City'''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False,)
