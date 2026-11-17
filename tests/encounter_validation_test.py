import pytest
import validate
import pandas as pd

encounters_df = pd.read_csv('./Data/invalid/encounters.csv')
patients_df = pd.read_csv('./Data/invalid/patients.csv')
organizations_df = pd.read_csv('./Data/invalid/organizations.csv')

@pytest.mark.parametrize(
    "column, expected_count",
    [
        ("Id", 3),
        ("START", 2),
        ("PATIENT", 1),
        ("ORGANIZATION", 1),
        ("PROVIDER", 0),
        ("ENCOUNTERCLASS", 1),
        ("CODE", 0)
    ]
)

def test_patient_missing_values(column, expected_count):
    result = validate.validate_missing_data(
        encounters_df, [column]
    )
    assert len(result) == expected_count

def test_len_missing_patient_and_org_encounter():
    result = validate.validate_missing_data(encounters_df, ['PATIENT', 'ORGANIZATION'])
    assert(len(result) == 2)

def test_len_missing_id_and_org_encounter():
    result = validate.validate_missing_data(encounters_df, ['Id', 'ORGANIZATION'])
    assert(len(result) == 3)

def test_len_duplicate_id_encounter():
    result = validate.validate_duplicate_ids(encounters_df, "Id")
    assert(len(result) == 12)

def test_len_bad_stop_date_encounter():
    result = validate.validate_encounter_dates(encounters_df, 'START', 'STOP')
    assert(len(result) == 3)

def test_invalid_patient_id_encounter():
    assert(len(validate.encounter_ref_invalid_patient_or_org(encounters_df, patients_df, organizations_df)) == 3)