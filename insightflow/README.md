# InsightFlow

Mini product analytics platform built with Django + DRF.

## Features

- Event-based analytics
- DAU calculation
- Funnel analysis
- D1 retention
- Revenue analytics
- CSV ingestion via management command
- REST API endpoints
- Minimal web dashboard template

## Product Scenario

The project simulates analytics for an online learning platform.

Users can:
- open app
- sign up
- start courses
- complete lessons
- purchase subscriptions

The system tracks events and calculates key product metrics.

## Tech Stack

- Python 3.12+
- Django
- Django REST Framework
- Pandas
- SQLite

## Architecture

The project uses an event-driven data model (`Event`) and a service layer:

- API controllers live in `analytics_app/views.py`
- Business logic is intentionally moved to `analytics_app/services/`
- Data ingestion is done by `load_events` management command

This separation makes the code easier to scale and test:
API layer handles transport, services handle product calculations.

## Metrics

- **DAU**: unique users per day
- **Funnel**: conversion through `opens_app -> signup -> start_course -> subscribe`
- **Retention**: D1 retention per cohort day
- **Revenue**:
  - total revenue
  - revenue by day
  - ARPU

## Project Structure

```text
insightflow/
├── backend/
│   ├── manage.py
│   ├── requirements.txt
│   ├── config/
│   └── analytics_app/
├── data/
│   └── sample_events.csv
├── screenshots/
└── README.md
```

## Installation

```bash
cd insightflow/backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py load_events
python manage.py runserver
```

## API Endpoints

- `GET /api/metrics/dau/`
- `GET /api/metrics/funnel/`
- `GET /api/metrics/retention/`
- `GET /api/metrics/revenue/`
- `GET /api/dashboard/`

Optional segment filters:

- `?platform=ios`
- `?country=RU`

Example:

`/api/metrics/dau/?platform=ios&country=RU`

## Why This Project

InsightFlow demonstrates:
- product analytics thinking
- event-driven architecture
- backend engineering skills
- data processing and metric calculation
- REST API design

## Next Improvements

- Swagger / OpenAPI (`drf-spectacular`)
- Dockerfile + docker-compose
- PostgreSQL migration
- caching for expensive metric endpoints
