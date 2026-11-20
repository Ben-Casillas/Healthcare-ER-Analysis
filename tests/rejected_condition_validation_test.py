def test_encounter_rejection_has_expected_amount(rejected_conditions_df):
    assert(len(rejected_conditions_df) == 5)

def test_multiple_reason_appear_in_rejection_reason(rejected_conditions_df):
    rejection_reason = rejected_conditions_df.at[3, "rejection_reason"]
    assert(rejection_reason.__contains__("Missing START Column"))
    assert(rejection_reason.__contains__("Missing CODE Column"))

def test_all_records_have_reason(rejected_conditions_df):
    null_reasons = rejected_conditions_df[rejected_conditions_df['rejection_reason'].isna()]
    assert(len(null_reasons) == 0)