import pytest


def test_encounter_rejection_has_expected_amount(rejected_encounters_df):
    assert(len(rejected_encounters_df) == 12)

def test_multiple_reason_appear_in_rejection_reason(rejected_encounters_df):
    rejection_reason = rejected_encounters_df.at[11, "rejection_reason"]
    assert(rejection_reason.__contains__("Duplicate ID"))
    assert(rejection_reason.__contains__("Missing Id Column"))
    assert(rejection_reason.__contains__("Missing START Column"))
    assert(rejection_reason.__contains__("Missing ORGANIZATION Column"))

def test_all_records_have_reason(rejected_encounters_df):
    null_reasons = rejected_encounters_df[rejected_encounters_df['rejection_reason'].isna()]
    assert(len(null_reasons) == 0)

def test_all_duplicate_ids_are_distinguishable(rejected_encounters_df):
    duplicate_ids = rejected_encounters_df[rejected_encounters_df.duplicated(subset=["Id"], keep=False)]
    duplicate_id_count = len(duplicate_ids)
    unique_duplicate_source_row = duplicate_ids["_source_row"].nunique()
    assert(unique_duplicate_source_row == duplicate_id_count)