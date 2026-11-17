import pytest
import validate
import pandas as pd
patients_df = pd.read_csv('./Data/invalid/patients.csv')
empty_df = pd.DataFrame(columns=list(patients_df.columns))

@pytest.mark.parametrize(
    "column, expected_count",
    [
        ("ID", 2),
        ("BIRTHDATE", 2),
        ("SSN", 0),
        ("FIRST", 0),
        ("LAST", 0)
    ]
)

def test_invalid_patient_missing_values(invalid_patients_df, column, expected_count):
    result = validate.validate_missing_data(
        invalid_patients_df, [column]
    )
    assert len(result) == expected_count

def test_invalid_len_missing_id_and_birthdate_patient(invalid_patients_df):
    result = validate.validate_missing_data(invalid_patients_df, ['Id', 'BIRTHDATE'])
    assert(len(result) == 3)

def test_invalid_patient_duplicate_ids(invalid_patients_df):
    result = validate.validate_duplicate_ids(invalid_patients_df, 'Id')
    assert(len(result) == 9)
    assert result['Id'].duplicated(keep=False).all()

# test against an empty DF
def test_empty_patients():
    result = validate.validate_missing_data(empty_df, ['Id', 'BIRTHDATE', 'SSN', 'FIRST', 'LAST'])
    assert(len(result) == 0)