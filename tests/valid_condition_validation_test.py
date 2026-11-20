import pytest
import validate

@pytest.mark.parametrize(
    "column, expected_count",
    [
        ("START", 0),
        ("PATIENT", 0),
        ("ENCOUNTER", 0),
        ("SYSTEM", 0),
        ("CODE", 0)
    ]
)

def test_valid_condition_missing_values(valid_conditions_df, column, expected_count):
    result = validate.validate_missing_data(
        valid_conditions_df, [column]
    )
    assert len(result) == expected_count

def test_valid_len_missing_start_and_patient_condition(valid_conditions_df):
    result = validate.validate_missing_data(valid_conditions_df, ['START', 'PATIENT'])
    assert(len(result) == 0)

def test_valid_patient_id_condition(valid_conditions_df, valid_patients_df, valid_encounters_df):
    result = validate.conditions_ref_invalid_patient_or_encounter(valid_conditions_df, valid_patients_df, valid_encounters_df)
    assert(len(result) == 0)


#test if blank patient in condition is marked as relationship to blank id patient
#test if blank encounter in encounter is marked as relationship to blank id encounter