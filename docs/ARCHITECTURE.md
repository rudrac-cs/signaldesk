# Architecture (initial)

`React UI` → HTTP `FastAPI` → `Synthetic data + simple rules`

PostgreSQL will be added for persistent review actions in a later sprint. Jack Henry integration is a possible sandbox-backed adapter, **not** a dependency of the initial demo.

## Transaction JSON contract
- `id`: string
- `merchant`: string
- `amount`: number (USD, demo only)
- `currency`: string
- `timestamp`: ISO datetime
- `risk_level`: `low | medium | high`
- `risk_score`: integer from 0 to 100
- `reasons`: list of explanatory strings
- `status`: `pending_review`

## Proposed flow
Synthetic transactions → transparent, testable risk heuristics → review queue → explanation panel → documented review decision.

## Non-goals for prototype
Production-grade risk scoring, legal compliance certification, customer identity verification, payment execution, and real money movement.
