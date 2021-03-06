#!/usr/bin/python3
"""
This module prints the first state using SWLAlchemy
"""
import MySQLdb
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    if (len(sys.argv) == 4):
        user, password, database = (sys.argv[1], sys.argv[2], sys.argv[3])
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                user, password, database))
        SessionMkr = sessionmaker(bind=engine)
        session = SessionMkr()
        state = session.query(State).first()
        if (state is not None):
            print("{}: {}".format(state.id, state.name))
        else:
            print("Nothing")
