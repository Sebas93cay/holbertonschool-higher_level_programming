#!/usr/bin/python3
"""
This module prints the first state using SWLAlchemy
"""
import sys
from relationship_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City


if __name__ == '__main__':
    if (len(sys.argv) == 4):
        user, password, database = (sys.argv[1],
                                    sys.argv[2], sys.argv[3])
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                user, password, database))
        Base.metadata.create_all(engine)
        SessionMkr = sessionmaker(bind=engine)
        session = SessionMkr()
        cities = session.query(City, State.name).join(State).all()
        for c in cities:
            print("{}: {} -> {}".format(c[0].id, c[0].name, c[1]))
