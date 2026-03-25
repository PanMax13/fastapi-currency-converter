from pydantic import BaseModel

class ConvertResponse(BaseModel):
    from_currency: str
    to_currency: str
    amount: float
    result: float