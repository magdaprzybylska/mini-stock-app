import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

engine = create_engine(f"sqlite:///{BASE_DIR}/orders.db", echo=True)

session = scoped_session(
    sessionmaker(
        autoflush=False,
        autocommit=False,
        bind=engine
    )
)