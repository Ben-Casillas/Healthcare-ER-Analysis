import pytest
import validate

# TODO: test if blank patient/encounter in condition is marked as relationship to blank id patient/encounter
@pytest.mark.parametrize(
    "column, expected_count",
    [
        ("START", 1),
        ("PATIENT", 1),
        ("ENCOUNTER", 1),
        ("SYSTEM", 0),
        ("CODE", 1)
    ]
)

def test_invalid_condition_missing_values(invalid_conditions_df, column, expected_count):
    result = validate.validate_missing_data(
        invalid_conditions_df, [column]
    )
    assert len(result) == expected_count

def test_invalid_len_missing_start_and_patient_condition(invalid_conditions_df):
    result = validate.validate_missing_data(invalid_conditions_df, ['START', 'PATIENT'])
    assert(len(result) == 2)

def test_invalid_patient_id_condition(invalid_conditions_df, invalid_patients_df, invalid_encounters_df):
    result = validate.conditions_ref_invalid_patient_or_encounter(invalid_conditions_df, invalid_patients_df, invalid_encounters_df)
    assert(len(result) == 2)


#test if blank patient in condition is marked as relationship to blank id patient
#test if blank encounter in encounter is marked as relationship to blank id encounter