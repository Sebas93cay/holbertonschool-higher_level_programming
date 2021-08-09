#!/usr/bin/python3
"""
This is the model of cities with relationship
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base, State


class City(Base):
    """
    City Class
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship("State", back_populates="cities")

    def __repr__(self) -> str:
        return "City {}: {} state_id:{}".format(self.id, self.name,
                                                self.state_id)

# State.cities = relationship("City", order_by=City.id, back_populates="state",
        # cascade="all, delete, delete-orphan")
