#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column('name', String(128), nullable=False)
        state_id = Column('state_id', String(60),
                          ForeignKey('states.id'), nullable=False)
    else:
        state_id = ""
        name = ""
