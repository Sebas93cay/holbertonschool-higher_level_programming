#!/usr/bin/python3
"""
This module adds a new State to the table states
"""

import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    if (len(sys.argv) == 5):
        user, password, database, state_name = (sys.argv[1],
                                                sys.argv[2],
                                                sys.argv[3],
                                                sys.argv[4])
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                user, password, database))
        SessionMkr = sessionmaker(bind=engine)
        session = SessionMkr()
        state = session.query(State).filter(State.name == state_name).first()
        if (state):
            print(state.id)
        else:
            print('Not found')
