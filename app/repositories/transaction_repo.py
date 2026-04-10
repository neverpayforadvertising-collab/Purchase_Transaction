from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.models import Transaction

class TransactionRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, transaction: Transaction):
        self.db.add(transaction)
        await self.db.commit()
        await self.db.refresh(transaction)
        return transaction

    async def get_by_id(self, tx_id: str):
        result = await self.db.execute(
            select(Transaction).where(Transaction.id == tx_id)
        )
        return result.scalar_one_or_none()