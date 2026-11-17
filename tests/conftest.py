import pytest
import pandas as pd


@pytest.fixture
def invalid_patients_df():
    return pd.read_csv(
        "./Data/invalid/patients.csv"
    )

@pytest.fixture
def valid_patients_df():
    return pd.read_csv(
        "./Data/raw/patients.csv"
    )

@pytest.fixture
def invalid_encounters_df():
    return pd.read_csv(
        "./Data/invalid/encounters.csv"
    )

@pytest.fixture
def valid_encounters_df():
    return pd.read_csv(
        "./Data/raw/encounters.csv"
    )

@pytest.fixture
def invalid_organizations_df():
    return pd.read_csv(
        "./Data/invalid/organizations.csv"
    )

@pytest.fixture
def valid_organizations_df():
    return pd.read_csv(
        "./Data/raw/organizations.csv"
    )

@pytest.fixture
def invalid_conditions_df():
    return pd.read_csv(
        "./Data/invalid/conditions.csv"
    )

@pytest.fixture
def valid_conditions_df():
    return pd.read_csv(
        "./Data/raw/conditions.csv"
    )