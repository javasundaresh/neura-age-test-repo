from __future__ import annotations

import pandas as pd


def compute_full_name(df: pd.DataFrame) -> pd.DataFrame:
    # Intentional error: references a non-existent column 'frist_name' (typo)
    out = df.copy()
    out["full_name"] = out["frist_name"] + " " + out["last_name"]  # noqa: F821
    return out


def faulty_ratio(df: pd.DataFrame) -> pd.DataFrame:
    # Intentional runtime error: division by zero when column has zeros
    out = df.copy()
    out["faulty_ratio"] = out["user_id"] / 0
    return out
