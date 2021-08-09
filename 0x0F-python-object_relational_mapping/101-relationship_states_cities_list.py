# #!/usr/bin/python3
# """
# This module prints the first state using SWLAlchemy
# """
# import sys
# from relationship_state import State, Base
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from relationship_city import City


# if __name__ == '__main__':
# if (len(sys.argv) == 4):
# user, password, database = (sys.argv[1],
# sys.argv[2], sys.argv[3])
# engine = create_engine(
# 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
# user, password, database), pool_pre_ping=True)
# SessionMkr = sessionmaker(bind=engine)
# session = SessionMkr()
# states = session.query(State).order_by(State.id).all()
# for s in states:
# print("{}: {}".format(s.id, s.name))
# for c in s.cities:
# print("    {}: {}".format(c.id, c.name))
# session.close()

#!/usr/bin/python3
"""Script that lists all States with their City names and ids
from database hbtn_0e_101_usa."""
from sys import argv
from relationship_state import State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user, password, dbname = argv[1], argv[2], argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(user, password, dbname), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print("{:d}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {:d}: {}".format(city.id, city.name))

    session.close()
