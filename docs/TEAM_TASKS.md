# First sprint: four-person team

## Shared objective
Demo a reviewer who can open a transaction, see a transparent risk explanation, and record a proposed review outcome (no real bank actions).

## Issue 1: Frontend filters and states
**Owner:** Frontend
- Add search by merchant/id and filter by risk level.
- Handle loading, errors, and empty results.
- Acceptance: filters work with the synthetic API response.

## Issue 2: Backend review workflow
**Owner:** Backend
- Propose `ReviewDecision` schema with `transaction_id`, `decision`, `note`, `reviewer`, `timestamp`.
- Add API POST/GET for decisions, initially in memory. No authentication claims.
- Validate inputs and add tests.
- Acceptance: API docs and tests demonstrate workflow.

## Issue 3: Risk rules and synthetic cases
**Owner:** Risk/data
- Move demo risk rules into `backend/app/risk.py` with deterministic functions.
- Include edge cases and tests. Document thresholds as illustrative.
- Acceptance: reasons are legible and outcomes reproducible.

## Issue 4: Integration and documentation
**Owner:** Lead
- Establish GitHub issues, branch protection if available, README checks.
- Define response contracts and review PRs.
- Research only authorized Jack Henry sandbox options and document assumptions.
- Acceptance: fresh clone runs on teammate laptops and all changes land via PR.

## Collaboration rules
- Never push credentials, sensitive banking data, or `.env` files.
- Branch from updated `main`: `git switch -c feature/short-description`.
- Keep each PR narrow; mention which issue it closes.
- Run backend tests and frontend build before review.
- Request at least one teammate's review before merge.
