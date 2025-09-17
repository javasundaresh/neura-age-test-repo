from __future__ import annotations

import os
import pandas as pd
from typing import Optional


def ensure_dir_exists(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)


def read_csv(filepath: str, dtype: Optional[dict] = None) -> pd.DataFrame:
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"CSV not found: {filepath}")
    return pd.read_csv(filepath, dtype=dtype)


def write_csv(df: pd.DataFrame, filepath: str, index: bool = False) -> None:
    ensure_dir_exists(os.path.dirname(filepath))
    df.to_csv(filepath, index=index)
