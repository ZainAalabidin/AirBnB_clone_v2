#!/usr/bin/python3
""" City Module for HBNB project """
from models.place import Place
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    if models.HBNB_TYPE_STORAGE == "db":
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="city", cascade="all, delete, delete-orphan")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """ initialaizition of City class """
        super().__init__(*args, **kwargs)

