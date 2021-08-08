#!/usr/bin/python3
"""
This module list all cities with its respective state
"""

import sys
from model_state import State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    if (len(sys.argv) == 4):
        user, password, database = (sys.argv[1],
                                    sys.argv[2], sys.argv[3])
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                user, password, database))
        SessionMkr = sessionmaker(bind=engine)
        session = SessionMkr()
        cities = session.query(City, State).join(State).all()
        for c, s in cities:
            print("{}: ({}) {}".format(c.name, c.id, s.name))
