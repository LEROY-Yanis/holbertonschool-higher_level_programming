#!/usr/bin/python3
"""Script that changes the name of a State object with id 2."""

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
        state = session.query(State).filter(State.id == 2).first()
        if state is not None:
            state.name = "New Mexico"
            session.commit()
