from app.repositories.transaction_repo import TransactionRepository
from app.db.models import Transaction
from app.domain.exceptions import NotFoundError

class TransactionService:
    def __init__(self, repo: TransactionRepository):
        self.repo = repo

    async def create(self, data):
        tx = Transaction(**data.dict())
        return await self.repo.create(tx)

    async def get(self, tx_id: str):
        tx = await self.repo.get_by_id(tx_id)
        if not tx:
            raise NotFoundError("Transaction not found")
        return tx