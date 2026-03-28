#!/usr/bin/python3
"""Script that deletes all State objects containing the letter a."""

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
        states = session.query(State).filter(State.name.like("%a%")).all()
        for state in states:
            session.delete(state)
        session.commit()
