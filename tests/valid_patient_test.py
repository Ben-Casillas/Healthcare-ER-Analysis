import pytest
import validate
import pandas as pd
# valid_patients_df = pd.read_csv('./Data/raw/patients.csv')

@pytest.mark.parametrize(
    "column, expected_count",
    [
        ("Id", 0),
        ("BIRTHDATE", 0),
        ("SSN", 0),
        ("FIRST", 0),
        ("LAST", 0)
    ]
)

def test_invalid_patient_missing_values(valid_patients_df, column, expected_count):
    result = validate.validate_missing_data(
        valid_patients_df, [column]
    )
    assert len(result) == expected_count

def test_invalid_len_missing_id_and_birthdate_patient(valid_patients_df):
    result = validate.validate_missing_data(valid_patients_df, ['Id', 'BIRTHDATE'])
    assert(len(result) == 0)

def test_invalid_patient_duplicate_ids(valid_patients_df):
    result = validate.validate_duplicate_ids(valid_patients_df, 'Id')
    assert(len(result) == 0)
    assert result['Id'].duplicated(keep=False).all()
