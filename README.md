# SignalDesk

A prototype fraud-review dashboard for bank employees. SignalDesk highlights potentially suspicious transactions, explains the signals behind each flag, and helps reviewers make documented decisions.

**Status:** Starter repository for the FinTech UTD student team. All transactions are **synthetic sample data**. The rules are illustrative, not production fraud detection.

## What works on day one
- React + TypeScript + Vite reviewer dashboard
- FastAPI endpoint returning synthetic transactions and readable flag reasons
- Risk badges, transaction selection, and a detail pane
- Basic backend API test
- Optional PostgreSQL container for a later persistence milestone

## Quick start

### 1. Backend
Requires Python 3.10+.

```bash
cd backend
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Open http://localhost:8000/docs to test the API.

### 2. Frontend
Open a **second terminal**. Requires Node.js 20.19+ or 22.12+.

```bash
cd frontend
npm install
cp .env.example .env   # Windows PowerShell: Copy-Item .env.example .env
npm run dev
```

Open the local URL Vite prints (usually http://localhost:5173).

### 3. Run tests
```bash
cd backend
pytest
```

### 4. Optional database (not needed to run the demo)
With Docker installed, from the repo root:

```bash
docker compose up -d db
```

Connection details for local development are in `docker-compose.yml`. Do not put real credentials or customer data in this repository.

## Folder map

```text
frontend/        React reviewer dashboard
backend/app/     FastAPI app, schemas, demo transaction data
backend/tests/   API tests
docs/            Scope, architecture, team tasks
.github/         Pull request template
```

## API
- `GET /health`: health check
- `GET /api/transactions`: synthetic transaction list with reasons and risk level
- `GET /api/transactions/{transaction_id}`: single transaction or 404

## Team Structure

SignalDesk is being developed by the FinTech UTD team, consisting of one Project Lead and four developers.

| Role | Responsibilities |
|---|---|
| Project Lead | Project planning, team coordination, task assignments, deadlines, pull request oversight, and Jack Henry communication |
| Frontend Developer | React/TypeScript dashboard, transaction tables, filtering, and investigation interface |
| Backend Developer | FastAPI endpoints, application logic, transaction review workflow, and external API integration |
| Database Engineer | PostgreSQL schema design, database migrations, transaction storage, relationships, and queries |
| Fraud Detection Engineer | Explainable fraud detection rules, risk scoring, synthetic scenarios, and evaluation |

## Development Workflow

1. Every developer should work on tasks assigned through GitHub Issues.
2. Create a separate `feature/...` branch for each task.
3. Do not push code changes directly to `main`.
4. Submit a pull request when work is ready for review.
5. Coordinate shared API contracts and database changes before implementation.
6. Never commit secrets, real banking credentials, or customer information.
7. Communicate blockers early and provide brief weekly progress updates.

See `docs/TEAM_TASKS.md` for current assignments and deadlines.

## Jack Henry integration
Potential future integration only, subject to approved developer platform access, documentation, and sandbox permissions. Keep a mock-data mode; never assume a live banking API is available.

## Safety and scope
This is a **human-in-the-loop educational prototype**. A risk score is not proof of fraud. Do not ingest real customer PII, real account credentials, or production bank data. Do not implement automatic account restrictions or payment blocking.
