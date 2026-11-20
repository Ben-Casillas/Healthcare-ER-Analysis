import pytest
import validate

@pytest.mark.parametrize(
    "column, expected_count",
    [
        ("Id", 0),
        ("START", 0),
        ("PATIENT", 0),
        ("ORGANIZATION", 0),
        ("PROVIDER", 0),
        ("ENCOUNTERCLASS", 0),
        ("CODE", 0)
    ]
)

def test_patient_missing_values(valid_encounters_df, column, expected_count):
    result = validate.validate_missing_data(
        valid_encounters_df, [column]
    )
    assert len(result) == expected_count

def test_len_missing_patient_and_org_encounter(valid_encounters_df):
    result = validate.validate_missing_data(valid_encounters_df, ['PATIENT', 'ORGANIZATION'])
    assert(len(result) == 0)

def test_len_missing_id_and_org_encounter(valid_encounters_df):
    result = validate.validate_missing_data(valid_encounters_df, ['Id', 'ORGANIZATION'])
    assert(len(result) == 0)

def test_len_duplicate_id_encounter(valid_encounters_df):
    result = validate.validate_duplicate_ids(valid_encounters_df, "Id")
    assert(len(result) == 0)

def test_len_bad_stop_date_encounter(valid_encounters_df):
    result = validate.validate_encounter_dates(valid_encounters_df, 'START', 'STOP')
    assert(len(result) == 0)

def test_valid_patient_id_encounter(valid_encounters_df, valid_patients_df, valid_organizations_df):
    assert(len(validate.encounter_ref_invalid_patient_or_org(valid_encounters_df, valid_patients_df, valid_organizations_df)) == 0)