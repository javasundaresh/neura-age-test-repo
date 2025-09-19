# Neura Age Test Repo (Data Engineering style)

This repository is a small data engineering style project used to test RCA (root cause analysis) tooling. It intentionally contains some faulty code and SQL for analysis.

## Layout

- `src/`
  - `config.py`: Paths and DB URL (SQLite in-memory by default)
  - `utils/io.py`: Helpers for reading/writing CSVs
  - `ingest/csv_to_db.py`: Load CSV from `data/raw` into DB table
  - `transforms/normalize_users.py`: Clean names and emails
  - `transforms/bad_calculation.py`: Intentionally faulty transformations
- `data/raw/users.csv`: Sample dataset
- `sql/ddl/create_users.sql`: DDL for `users`
- `sql/queries/good_user_counts.sql`: Valid query
- `sql/queries/bad_syntax.sql`: Intentionally broken SQL
- `dags/user_pipeline_dag.py`: Airflow-like DAG with intentional issues
- `tests/test_transforms.py`: Some tests (expecting failures)

## Setup

Python 3.11+ recommended.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Quick start

- Ingest sample data to DB (in-memory SQLite by default):
```bash
python -m src.ingest.csv_to_db
```

- Run tests (some are expected to fail by design):
```bash
pytest -q
```

Use these to validate error detection, tracing, and remediation suggestions in your RCA tool.