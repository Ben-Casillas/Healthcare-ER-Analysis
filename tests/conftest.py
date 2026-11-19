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

@pytest.fixture
def rejected_patients_df():
    return pd.read_csv(
        "./Data/rejected/patient_rejections.csv"
    )

@pytest.fixture
def rejected_encounters_df():
    return pd.read_csv(
        "./Data/rejected/encounter_rejections.csv"
    )

@pytest.fixture
def rejected_organizations_df():
    return pd.read_csv(
        "./Data/rejected/organization_rejections.csv"
    )

@pytest.fixture
def rejected_conditions_df():
    return pd.read_csv(
        "./Data/rejected/condition_rejections.csv"
    )