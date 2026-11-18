from typing import Literal
from pydantic import BaseModel

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .sample_data import TRANSACTIONS

app = FastAPI(title="SignalDesk API", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/api/transactions")
def list_transactions():
    return TRANSACTIONS


@app.get("/api/transactions/{transaction_id}")
def get_transaction(transaction_id: str):
    for transaction in TRANSACTIONS:
        if transaction["id"] == transaction_id:
            return transaction
    raise HTTPException(status_code=404, detail="Transaction not found")





class ReviewRequest(BaseModel):
    status: Literal["legitimate", "escalated"]


@app.patch("/api/transactions/{transaction_id}/review")
def review_transaction(transaction_id: str, review: ReviewRequest):
    for transaction in TRANSACTIONS:
        if transaction["id"] == transaction_id:
            transaction["status"] = review.status
            return transaction

    raise HTTPException(
        status_code=404,
        detail="Transaction not found"
    )



