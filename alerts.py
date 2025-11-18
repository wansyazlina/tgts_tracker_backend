from pydantic import BaseModel
from typing import List
from datetime import datetime

class Alert(BaseModel):
    accountNumber: str
    recipients: List[str]
    expiresAt: datetime
