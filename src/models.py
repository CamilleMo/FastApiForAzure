from sqlalchemy import Column, Integer, String

from .database import Base


class Customers(Base):
    __tablename__ = "customers"
    CustomerId = Column(Integer, primary_key=True, index=True)
    FirstName = Column(String)
    LastName = Column(String)
    Company = Column(String)
    Address = Column(String)
    City = Column(String)
    Country = Column(String)
    PostalCode = Column(String)
    Phone = Column(String)
    Fax = Column(String)
    Email = Column(String)
    SupportRepId = Column(Integer)
