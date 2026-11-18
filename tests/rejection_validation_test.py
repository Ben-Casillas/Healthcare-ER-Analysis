import pytest



#rejected records
# Test                                   Expected result
# One invalid record	                Appears in rejection report
# One record fails multiple checks	    Appears once with multiple reasons
# No invalid records	                 Empty rejection report
# Every rejected record	                  Has a rejection reason
# Two records have duplicate IDs	    Both remain distinguishable
# Missing record ID	                    Record still appears in report

def test_multiple_reason_appear_in_rejection_reason(rejected_patients_df):
    rejection_reason = rejected_patients_df.at[1, "rejection_reason"]