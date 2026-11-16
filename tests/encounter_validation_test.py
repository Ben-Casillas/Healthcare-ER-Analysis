import pytest
import validate
import pandas as pd

encounters_df = pd.read_csv('./Data/invalid/encounters.csv')
patients_df = pd.read_csv('./Data/invalid/patients.csv')
organizations_df = pd.read_csv('./Data/invalid/organizations.csv')

def test_len_missing_id_encounter():
    assert(len(validate.validate_missing_data(encounters_df, ['Id'])) == 3)

def test_len_missing_start_encounter():
        assert(len(validate.validate_missing_data(encounters_df, ['START'])) == 2)

def test_len_missing_patient_encounter():
    assert(len(validate.validate_missing_data(encounters_df, ['PATIENT'])) == 1)

def test_len_missing_org_encounter():
        assert(len(validate.validate_missing_data(encounters_df, ['ORGANIZATION'])) == 1)

def test_len_missing_provider_encounter():
    with pytest.raises(AssertionError):
        assert(len(validate.validate_missing_data(encounters_df, ['PROVIDER'])) != 0)

def test_len_missing_encounterclass_encounter():
    assert(len(validate.validate_missing_data(encounters_df, ['ENCOUNTERCLASS'])) == 1)

def test_len_missing_code_encounter():
    with pytest.raises(AssertionError):
        assert(len(validate.validate_missing_data(encounters_df, ['CODE'])) != 0)

def test_len_missing_patient_and_org_encounter():
    assert(len(validate.validate_missing_data(encounters_df, ['PATIENT', 'ORGANIZATION'])) == 2)

def test_len_missing_id_and_org_encounter():
    assert(len(validate.validate_missing_data(encounters_df, ['Id', 'ORGANIZATION'])) == 3)

def test_len_duplicate_id_encounter():
    assert(len(validate.validate_duplicate_ids(encounters_df, "Id")) == 12)

def test_len_bad_stop_date_encounter():
    assert(len(validate.validate_encounter_dates(encounters_df, 'START', 'STOP')) == 3)
# ask people what other tests i should run

def test_invalid_patient_id_encounter():
    assert(len(validate.encounter_ref_invalid_patient_or_org(encounters_df, patients_df, organizations_df)) == 3)