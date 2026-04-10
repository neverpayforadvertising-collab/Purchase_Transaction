# Purchase Transaction API

A production-ready backend service for storing purchase transactions and retrieving them with historical currency conversion using U.S. Treasury exchange rates.

---

## Features

- Store purchase transactions (USD)
- Retrieve transactions converted to target currency
- Historical exchange rate resolution (≤ purchase date, within 6 months)
- Async architecture (FastAPI + SQLAlchemy async)
- Repository pattern + dependency injection
- In-memory caching for exchange rates
- Domain-level error handling
- Dockerized
- CI pipeline (GitHub Actions)
- Fully testable (pytest)

---

## Architecture

The project follows clean architecture principles

## How to run

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload