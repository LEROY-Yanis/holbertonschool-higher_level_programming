#!/usr/bin/python3
"""Script that lists all City objects with their State name."""

from sys import argv

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3]
        ),
        pool_pre_ping=True,
    )

    Base.metadata.create_all(engine)

    with Session(engine) as session:
        query = (
            session.query(State.name, City.id, City.name)
            .join(City, State.id == City.state_id)
            .order_by(City.id.asc())
            .all()
        )

        for state_name, city_id, city_name in query:
            print("{}: ({}) {}".format(state_name, city_id, city_name))
