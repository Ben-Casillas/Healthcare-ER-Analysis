import pytest
import pandas as pd


@pytest.fixture
def patients_df():
    return pd.read_csv(
        "./Data/invalid/patients.csv"
    )
