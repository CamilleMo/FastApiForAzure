from typing import Optional
from pydantic import BaseModel


class Customers(BaseModel):
    CustomerId: Optional[int]
    FirstName: Optional[str]
    LastName: Optional[str]
    Company: Optional[str]
    Address: Optional[str]
    City: Optional[str]
    Country: Optional[str]
    PostalCode: Optional[str]
    Phone: Optional[str]
    Fax: Optional[str]
    Email: Optional[str]
    SupportRepId: Optional[int]

    class Config:
        orm_mode = True
