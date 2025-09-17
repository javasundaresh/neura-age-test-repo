from __future__ import annotations

import os
from typing import Final

# Basic configuration used by scripts
DB_URL: Final[str] = os.getenv(
    "DB_URL",
    # In-memory SQLite by default for simplicity
    "sqlite+pysqlite:///:memory:",
)

DATA_DIR: Final[str] = os.getenv("DATA_DIR", os.path.join(os.getcwd(), "data"))
RAW_DIR: Final[str] = os.path.join(DATA_DIR, "raw")
PROCESSED_DIR: Final[str] = os.path.join(DATA_DIR, "processed")
