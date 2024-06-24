#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey


class State(BaseModel, Base):
    """State class"""

    __tablename__ = "states"

    if models.HBNB_TYPE_STORAGE == "db":
        name = Column(String(128), nullable=False)
        cities = relationship(
            "City", backref="state", cascade="all, delete, delete-orphan"
        )
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializing state model"""
        super().__init__(*args, **kwargs)

    if models.HBNB_TYPE_STORAGE != "db":

        @property
        def cities(self):
            """
            return the list of City objects from storage
            linked to the current State
            """
            CityList = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    CityList.append(city)
            return CityList
