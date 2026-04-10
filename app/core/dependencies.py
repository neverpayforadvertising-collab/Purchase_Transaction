from fastapi import Depends
from app.db.session import get_db
from app.repositories.transaction_repo import TransactionRepository
from app.services.transaction_service import TransactionService
from app.services.exchange_service import ExchangeService
from app.core.config import settings


async def get_transaction_service(db=Depends(get_db)):
    repo = TransactionRepository(db)
    return TransactionService(repo)


def get_exchange_service():
    return ExchangeService(settings.treasury_api_url)