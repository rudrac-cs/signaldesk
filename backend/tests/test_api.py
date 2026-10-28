from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    assert client.get("/health").json() == {"status": "ok"}


def test_transactions_have_explanations():
    response = client.get("/api/transactions")
    assert response.status_code == 200
    transactions = response.json()
    assert transactions
    assert all(t["reasons"] and 0 <= t["risk_score"] <= 100 for t in transactions)


def test_unknown_transaction_returns_404():
    assert client.get("/api/transactions/not-real").status_code == 404
