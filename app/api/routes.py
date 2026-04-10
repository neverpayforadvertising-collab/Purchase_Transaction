from fastapi import APIRouter, Depends
from app.schemas.transaction import TransactionCreate
from app.core.dependencies import get_transaction_service, get_exchange_service

router = APIRouter()

@router.post("/transactions")
async def create(tx: TransactionCreate, service=Depends(get_transaction_service)):
    return await service.create(tx)


@router.get("/transactions/{tx_id}")
async def get(tx_id: str, currency: str,
              tx_service=Depends(get_transaction_service),
              ex_service=Depends(get_exchange_service)):

    tx = await tx_service.get(tx_id)
    return await ex_service.convert(tx, currency)