from __future__ import annotations

import pandas as pd
import pytest

from src.transforms.normalize_users import normalize_users
from src.transforms.bad_calculation import compute_full_name, faulty_ratio


def test_normalize_users_lowercases_email():
    df = pd.DataFrame({
        "user_id": [1],
        "first_name": [" ADA  "],
        "last_name": ["  LOVELACE"],
        "email": ["ADA@EXAMPLE.COM"],
    })
    out = normalize_users(df)
    assert out.loc[0, "email"] == "ada@example.com"


def test_compute_full_name_fails_due_to_typo():
    df = pd.DataFrame({
        "user_id": [1],
        "first_name": ["Ada"],
        "last_name": ["Lovelace"],
        "email": ["ada@example.com"],
    })
    with pytest.raises(KeyError):
        compute_full_name(df)


def test_faulty_ratio_division_by_zero():
    df = pd.DataFrame({
        "user_id": [0],
        "first_name": ["Ada"],
        "last_name": ["Lovelace"],
        "email": ["ada@example.com"],
    })
    with pytest.raises(ZeroDivisionError):
        faulty_ratio(df)
