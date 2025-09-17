from __future__ import annotations

import os
from sqlalchemy import create_engine

from src.config import DB_URL, RAW_DIR
from src.utils.io import read_csv


def load_csv_to_db(csv_filename: str, table_name: str) -> int:
    """Load a CSV from data/raw into a database table.

    Returns number of rows inserted.
    """
    csv_path = os.path.join(RAW_DIR, csv_filename)
    df = read_csv(csv_path)

    engine = create_engine(DB_URL)
    with engine.begin() as conn:
        df.to_sql(table_name, con=conn, if_exists="replace", index=False)
        return len(df)


if __name__ == "__main__":
    inserted = load_csv_to_db("users.csv", "users")
    print(f"Inserted {inserted} rows into users")
