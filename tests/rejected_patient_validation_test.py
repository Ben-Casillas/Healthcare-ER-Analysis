# TODO: test for an empty rejection report

def test_patient_rejection_has_expected_amount(rejected_patients_df):
    assert(len(rejected_patients_df) == 9)

def test_multiple_reason_appear_in_rejection_reason(rejected_patients_df):
    rejection_reason = rejected_patients_df.at[1, "rejection_reason"]
    assert(rejection_reason.__contains__("Duplicate ID"))
    assert(rejection_reason.__contains__("Missing Id Column"))

def test_all_records_have_reason(rejected_patients_df):
    null_reasons = rejected_patients_df[rejected_patients_df['rejection_reason'].isna()]
    assert(len(null_reasons) == 0)

def test_all_duplicate_ids_are_distinguishable(rejected_patients_df):
    duplicate_ids = rejected_patients_df[rejected_patients_df.duplicated(subset=["Id"], keep=False)]
    duplicate_id_count = len(duplicate_ids)
    unique_duplicate_source_row = duplicate_ids["_source_row"].nunique()
    assert(unique_duplicate_source_row == duplicate_id_count)