from sqlalchemy.orm import declarative_base

from config import session

Model = declarative_base()
Model.query = session.query_property()

class Base(Model):
    __abstract__ = True
