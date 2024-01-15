from sqlalchemy import Column, Integer, Float, String

from models.base import Base

# set up class for database model
class Order(Base):
    __tablename__ = "orders"

    id = Column("id", Integer, primary_key=True)
    transaction_type = Column("transaction_type", String)
    price = Column("price", Float)
    quantity = Column("quantity", Integer)

    def __repr__(self): 
        return f"id: {self.id}, transaction_type: {self.transaction_type}, price: {self.price}, quantity: {self.quantity}"
