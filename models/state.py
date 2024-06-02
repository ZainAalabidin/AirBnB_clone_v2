#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey


class State(BaseModel, Base):
    """ State class """
    if models.storage_type = "db":
        __tablename__ = 'state'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """ initializing state model"""
        super().__init__(*args, **kwargs)

    if models.storage_type != "db":
        @property
        def cities(self):
            """
            return the list of City objects from storage
            linked to the current State
            """
            CityList = []
            cities = models.storage.all(City)
            for city  in cities.values():
                if city.state_id == self.id:
                    CityList.append(city)
            return CityList
