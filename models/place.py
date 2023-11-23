#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from os import getenv
import models


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128))
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []


    # if getenv("HBNB_TYPE_STORAGE") == "db":
    #    reviews = relationship(
    #        "Review",
    #        backref="place",
    #        cascade='delete'
    #    )
    # else:
    #    @property
    #    def reviews(self):
    #        """getter attribute for returning the list of reviews"""
    #        from models.review import Review
    #        stor = models.storage.all(Review)
    #        place_reviews = []
    #        for review in list(stor.values()):
    #            if review.place_id == self.id:
    #                place_reviews.append(review)
    #        return place_reviews
