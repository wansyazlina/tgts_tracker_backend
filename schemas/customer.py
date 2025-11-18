from pydantic import BaseModel

class Customer(BaseModel):
    accountNumber: str
    name: str
    currency: str
