#!/usr/bin/python3
"""
This module prints the first state using SWLAlchemy
"""
import sys
from relationship_state import State, Base
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker, aliased, selectinload
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

        state_name = 'California'
        city_name = 'San Francisco'

        # Create and add one state
        state = State(name=state_name)
        session.add(state)
        new_state = session.query(State).filter(
            State.name == state_name).order_by(State.id.desc()).first()
        # print(new_state)

        # Create and add one city
        city = City(name=city_name, state_id=new_state.id)
        session.add(city)
        # new_city = session.query(City).filter(City.name == city_name).one()

        # Commit new City and State
        session.commit()
        session.close()
