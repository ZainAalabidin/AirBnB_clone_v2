#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import os


if os.getenv("HBNB_TYPE_STORAGE") == "db":
    place_amenity = Table(
        "place_amenity",
        Base.metadata,
        Column(
            "place_id",
            String(60),
            ForeignKey("places.id", onupdate="CASCADE", ondelete="CASCADE"),
            primary_key=True,
        ),
        Column(
            "amenity_id",
            String(60),
            ForeignKey("amenities.id", onupdate="CASCADE", ondelete="CASCADE"),
            primary_key=True,
        ),
    )


class Place(BaseModel, Base):
    """A place to stay"""

    __tablename__ = "places"

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", back_populates="place", cascade="all, delete")
        amenities = relationship(
            "Amenity",
            secondary=place_amenity,
            back_populates="place_amenities",
            viewonly=False,
        )
        user = relationship("User", back_populates="places")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """Review getter - return list of filtered reviews."""
            reviews_instances = []
            reviews_dict = models.storage.all("Review")
            for key, value in reviews_dict.items():
                if self.id == value.place_id:
                    reviews_instances.append(value)
            return reviews_instances

        @property
        def amenities(self):
            """Review getter - return list of amenity instances"""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj):
            """Setter for amenity list"""
            if isinstance(obj, models.Amenity):
                self.amenity_ids.append(obj.id)

    def __init__(self, *args, **kwargs):
        """initializes place"""
        super().__init__(*args, **kwargs)
