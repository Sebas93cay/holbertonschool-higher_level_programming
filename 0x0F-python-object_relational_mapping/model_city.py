#!/usr/bin/python3
"""
This is the model of cities
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """
    City Class
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))

    state = relationship("State", back_populates="cities")

    def __repr__(self) -> str:
        return "City {}: {}".format(self.id, self.name)


State.cities = relationship("City", order_by=City.id, back_populates="state")
