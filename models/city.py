#!/usr/bin/python3
""" City Module for HBNB project """
import models
from models.base_model import BaseModel
from sqlalchemy import column, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel):
    """ The city class, contains state ID and name """
    if models.storage_type == "db":
        __tablename__ = 'cities'
        state_id = column(String(60), ForeignKey('state_id'), nullable=False)
        name = column(String(128), nullable=False)
        places = relationship("Place", Backref="cities")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """ initialaizition of City class """
        super.__init__(self, *args, **kwargs)

