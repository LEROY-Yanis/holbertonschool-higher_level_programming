#!/usr/bin/python3
"""Script that adds a new State object."""

from sys import argv

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3]
        ),
        pool_pre_ping=True,
    )

    Base.metadata.create_all(engine)

    with Session(engine) as session:
        new_state = State(name="Louisiana")
        session.add(new_state)
        session.commit()
        print(new_state.id)