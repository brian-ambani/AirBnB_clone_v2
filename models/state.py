#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models import storage
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    if models.storage_t == 'db':
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
             """Returns the list of City instances with state_id"""
             all_cities = storage.all(City)
             return [city for city in all_cities.values() if city.state_id == self.id]
