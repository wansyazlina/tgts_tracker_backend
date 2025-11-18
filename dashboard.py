from pydantic import BaseModel
from typing import List

class Dashboard(BaseModel):
    accountNumber: str
    fields: List[str]
