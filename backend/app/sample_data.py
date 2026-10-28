# Synthetic data only. Amounts, merchants, and signals are fictional.
TRANSACTIONS = [
    {"id": "TXN-1041", "merchant": "Metro Electronics", "amount": 2499.00, "currency": "USD", "timestamp": "2026-10-26T15:30:00Z", "risk_score": 91, "risk_level": "high", "reasons": ["Unusually large amount for this illustrative account", "Multiple demo transactions within a short window"], "status": "pending_review"},
    {"id": "TXN-1042", "merchant": "Northside Grocers", "amount": 58.20, "currency": "USD", "timestamp": "2026-10-26T14:10:00Z", "risk_score": 12, "risk_level": "low", "reasons": ["No demo risk rules triggered"], "status": "pending_review"},
    {"id": "TXN-1043", "merchant": "Brightline Travel", "amount": 860.50, "currency": "USD", "timestamp": "2026-10-25T22:45:00Z", "risk_score": 63, "risk_level": "medium", "reasons": ["Amount exceeds illustrative review threshold"], "status": "pending_review"},
    {"id": "TXN-1044", "merchant": "Lakeside Market", "amount": 120.00, "currency": "USD", "timestamp": "2026-10-25T18:05:00Z", "risk_score": 26, "risk_level": "low", "reasons": ["No significant demo risk indicators"], "status": "pending_review"},
    {"id": "TXN-1045", "merchant": "Summit Digital", "amount": 1750.00, "currency": "USD", "timestamp": "2026-10-25T10:20:00Z", "risk_score": 84, "risk_level": "high", "reasons": ["High-value transaction in synthetic data", "Illustrative unusual spending pattern"], "status": "pending_review"},
]
