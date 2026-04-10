from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_transaction():
    response = client.post("/transactions", json={
        "description": "Test",
        "transaction_date": "2024-03-10",
        "amount": 100.00
    })
    assert response.status_code == 200
    assert "id" in response.json()

def test_invalid_amount():
    response = client.post("/transactions", json={
        "description": "Test",
        "transaction_date": "2024-03-10",
        "amount": -10
    })
    assert response.status_code == 422