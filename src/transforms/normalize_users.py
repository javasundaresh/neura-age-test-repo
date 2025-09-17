from __future__ import annotations

import pandas as pd


def normalize_users(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["first_name"] = out["first_name"].str.strip().str.title()
    out["last_name"] = out["last_name"].str.strip().str.title()
    out["email"] = out["email"].str.lower()
    out["user_id"] = out["user_id"].astype(int)
    return out
