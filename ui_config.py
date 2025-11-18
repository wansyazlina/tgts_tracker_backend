from pydantic import BaseModel

class UIConfig(BaseModel):
    accountNumber: str
    fontName: str
    fontSize: int
    colorScheme: str
    preferredLanguage: str
