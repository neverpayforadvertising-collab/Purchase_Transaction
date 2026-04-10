from pydantic import BaseModel, constr, condecimal
from datetime import date

class TransactionCreate(BaseModel):
    description: constr(max_length=50)
    transaction_date: date
    amount: condecimal(gt=0, decimal_places=2)

class TransactionResponse(BaseModel):
    id: str
    description: str
    transaction_date: date
    amount_usd: float