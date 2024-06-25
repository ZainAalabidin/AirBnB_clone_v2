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

        @property
        def cities(self):
            from models import storage

            all_cities = storage.all("City").values()
            return [
                city
                for city in all_cities
                if getattr(city, "state_id", None) == self.id
            ]

    def __init__(self, *args, **kwargs):
        """initializing state model"""
        super().__init__(*args, **kwargs)
