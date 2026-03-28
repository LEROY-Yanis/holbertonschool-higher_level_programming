#!/usr/bin/env python3
"""Script that lists all State objects from a database."""

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
        for state in session.query(State).order_by(State.id.asc()).all():
            print("{}: {}".format(state.id, state.name))