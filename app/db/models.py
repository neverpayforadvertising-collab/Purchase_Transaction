from sqlalchemy import Column, String, Date, Numeric
from app.db.session import Base
import uuid

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    description = Column(String(50), nullable=False)
    transaction_date = Column(Date, nullable=False)
    amount_usd = Column(Numeric(10, 2), nullable=False)