import pytest
import validate
import pandas as pd

patients_df = pd.read_csv('./Data/invalid/patients.csv')

def test_len_missing_id_patient():
    assert(len(validate.validate_missing_data(patients_df, ['Id'])) == 2)

def test_len_missing_birthdate_patient():
    assert(len(validate.validate_missing_data(patients_df, ['BIRTHDATE'])) == 2)

def test_len_missing_ssn_patient():
    with pytest.raises(AssertionError):
        assert(len(validate.validate_missing_data(patients_df, ['SSN'])) != 0)

def test_len_missing_first_patient():
    with pytest.raises(AssertionError):
        assert(len(validate.validate_missing_data(patients_df, ['FIRST'])) != 0)

def test_len_missing_last_patient():
    with pytest.raises(AssertionError):
        assert(len(validate.validate_missing_data(patients_df, ['LAST'])) != 0)

def test_len_missing_id_and_birthdate_patient():
    assert(len(validate.validate_missing_data(patients_df, ['Id', 'BIRTHDATE'])) == 3)

def test_patient_duplicate_ids():
    assert(len(validate.validate_duplicate_ids(patients_df, 'Id')) == 9)

# ask people what other tests i should run