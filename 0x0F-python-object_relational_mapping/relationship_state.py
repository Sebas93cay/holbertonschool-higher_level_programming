#!/usr/bin/python3
"""
This is the model of states with relationship
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State Class
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    # cities = relationship("City", order_by=City.id, back_populates="state")
    cities = relationship("City", back_populates="state",
                          cascade="all, delete, delete-orphan")

    def __repr__(self) -> str:
        return "State {}: {}".format(self.id, self.name)


# City.state = relationship("State", back_populates="cities")
