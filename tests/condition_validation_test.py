import pytest
import validate
import pandas as pd

conditions_df = pd.read_csv('./Data/invalid/conditions.csv')
patients_df = pd.read_csv('./Data/invalid/patients.csv')
encounters_df = pd.read_csv('./Data/invalid/encounters.csv')

def test_len_missing_start_condition():
    assert(len(validate.validate_missing_data(conditions_df, ['START'])) == 1)

def test_len_missing_patient_condition():
    assert(len(validate.validate_missing_data(conditions_df, ['PATIENT'])) == 1)

def test_len_missing_encounter_condition():
    assert(len(validate.validate_missing_data(conditions_df, ['ENCOUNTER'])) == 1)

def test_len_missing_code_condition():
    assert(len(validate.validate_missing_data(conditions_df, ['CODE'])) == 1)

def test_len_missing_state_condition():
    with pytest.raises(AssertionError):
        assert(len(validate.validate_missing_data(conditions_df, ['DESCRIPTION'])) != 0)

def test_len_invalid_patient_id_condition():
    assert(len(validate.conditions_ref_invalid_patient_or_encounter(conditions_df, patients_df, encounters_df)) == 2)