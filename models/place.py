#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)
        # reviews = relationship("Review", cascade='all, delete,
        # delete-orphan', backref="place")

        # amenities = relationship("Amenity", secondary=place_amenity,
        # viewonly=False,
        # back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """ Returns list of reviews.id """
            var = models.storage.all()
            list_array = []
            result = []
            for key in var:
                review = key.replace('.', ' ')
                review = shlex.split(review)
                if (review[0] == 'Review'):
                    list_array.append(var[key])
            for elem in list_array:
                if (elem.place_id == self.id):
                    result.append(elem)
            return (result)

        @property
        def amenities(self):
            """ Returns list of amenity ids """
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """ Appends amenity ids to the attribute """
            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
