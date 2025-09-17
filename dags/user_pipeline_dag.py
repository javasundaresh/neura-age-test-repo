from __future__ import annotations

import os
from datetime import datetime

try:
    from airflow import DAG
    from airflow.operators.python import PythonOperator
except Exception:  # pragma: no cover
    # Minimal fallback stub so imports succeed if Airflow isn't installed
    class DAG:  # type: ignore
        def __init__(self, *_, **__):
            pass

    class PythonOperator:  # type: ignore
        def __init__(self, *_, **__):
            pass

from src.ingest.csv_to_db import load_csv_to_db
from src.transforms.normalize_users import normalize_users
from src.utils.io import read_csv, write_csv
from src.config import RAW_DIR, PROCESSED_DIR


def task_ingest():
    load_csv_to_db("users.csv", "users")


def task_transform():
    # Intentional minor bug: wrong filename for input to simulate FileNotFoundError
    df = read_csv(os.path.join(RAW_DIR, "user.csv"))
    out = normalize_users(df)
    write_csv(out, os.path.join(PROCESSED_DIR, "users_normalized.csv"))


def create_dag() -> DAG:
    default_args = {"start_date": datetime(2024, 1, 1)}
    dag = DAG(
        dag_id="user_pipeline_dag", schedule_interval=None, default_args=default_args
    )

    ingest = PythonOperator(task_id="ingest", python_callable=task_ingest, dag=dag)
    transform = PythonOperator(task_id="transform", python_callable=task_transform, dag=dag)

    # Intentional issue: dependency missing (ingest >> transform) so order isn't enforced
    # ingest >> transform

    return dag


dag = create_dag()
