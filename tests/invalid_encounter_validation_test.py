import pytest
import validate

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

def test_patient_missing_values(invalid_encounters_df, column, expected_count):
    result = validate.validate_missing_data(
        invalid_encounters_df, [column]
    )
    assert len(result) == expected_count

def test_len_missing_patient_and_org_encounter(invalid_encounters_df):
    result = validate.validate_missing_data(invalid_encounters_df, ['PATIENT', 'ORGANIZATION'])
    assert(len(result) == 2)

def test_len_missing_id_and_org_encounter(invalid_encounters_df):
    result = validate.validate_missing_data(invalid_encounters_df, ['Id', 'ORGANIZATION'])
    assert(len(result) == 3)

def test_len_duplicate_id_encounter(invalid_encounters_df):
    result = validate.validate_duplicate_ids(invalid_encounters_df, "Id")
    assert(len(result) == 12)

def test_len_bad_stop_date_encounter(invalid_encounters_df):
    result = validate.validate_encounter_dates(invalid_encounters_df, 'START', 'STOP')
    assert(len(result) == 3)

def test_invalid_patient_id_encounter(invalid_encounters_df, invalid_patients_df, invalid_organizations_df):
    assert(len(validate.encounter_ref_invalid_patient_or_org(invalid_encounters_df, invalid_patients_df, invalid_organizations_df)) == 3)

#test if blank patient in encounter is marked as relationship to blank id patient
#test if blank provider in encounter is marked as relationship to blank id provider
#test if blank payer in encounter is marked as relationship to blank id payer
#test if blank org in encounter is marked as relationship to blank id org