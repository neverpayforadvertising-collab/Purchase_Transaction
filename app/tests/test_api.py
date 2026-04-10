import pytest

@pytest.mark.asyncio
async def test_create_transaction(client):
    response = await client.post("/transactions", json={
        "description": "Test",
        "transaction_date": "2024-03-10",
        "amount": 100.0
    })
    assert response.status_code == 200