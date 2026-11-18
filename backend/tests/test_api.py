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



def test_review_transaction_legitimate():
    response = client.patch(
        "/api/transactions/TXN-1041/review",
        json={"status": "legitimate"}
    )

    assert response.status_code == 200
    assert response.json()["status"] == "legitimate"

    # Confirm GET returns the updated status
    get_response = client.get("/api/transactions/TXN-1041")
    assert get_response.status_code == 200
    assert get_response.json()["status"] == "legitimate"


def test_review_transaction_escalated():
    response = client.patch(
        "/api/transactions/TXN-1043/review",
        json={"status": "escalated"}
    )

    assert response.status_code == 200
    assert response.json()["status"] == "escalated"


def test_review_transaction_not_found():
    response = client.patch(
        "/api/transactions/does-not-exist/review",
        json={"status": "legitimate"}
    )

    assert response.status_code == 404


def test_review_transaction_invalid_status():
    response = client.patch(
        "/api/transactions/TXN-1041/review",
        json={"status": "invalid"}
    )

    assert response.status_code == 422
