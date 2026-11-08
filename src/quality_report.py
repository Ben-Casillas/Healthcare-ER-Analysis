import pandas as pd
import validate

patients_df = pd.read_csv('Data/invalid/patients.csv')
encounters_df = pd.read_csv('Data/invalid/encounters.csv')
organizations_df = pd.read_csv('Data/invalid/organizations.csv')
conditions_df = pd.read_csv('Data/invalid/conditions.csv')

#necessary since one of the validation rules check for mussing and dup en IDs, if i use Id to combine rejected
#encounters, it could cause problems
patients_df["_source_row"] = range(len(patients_df))
encounters_df["_source_row"] = range(len(encounters_df))
organizations_df["_source_row"] = range(len(organizations_df))
conditions_df["_source_row"] = range(len(conditions_df))

patient_validation_results = {
    "Missing Required Data": validate.validate_missing_data(patients_df, ['Id', 'BIRTHDATE', 'SSN', 'FIRST', 'LAST']),
    "Duplicate IDs": validate.validate_duplicate_ids(patients_df, 'Id')
}

encounter_validation_results = {
    "Missing Required Data": validate.validate_missing_data(encounters_df, ['Id', 'START', 'PATIENT', 'ORGANIZATION', 'PROVIDER']),
    "Duplicate IDs": validate.validate_duplicate_ids(encounters_df, 'Id'),
    "Invalid Encounter Dates": validate.validate_encounter_dates(encounters_df, 'START', 'STOP'),
    "Encounter References Invalid Patient or Organization": validate.encounter_ref_invalid_patient_or_org(encounters_df, patients_df, organizations_df)
}

condition_validation_results = {
    "Missing Required Data": validate.validate_missing_data(conditions_df, ['START', 'PATIENT', 'ENCOUNTER', 'CODE']),
    "Invalid Condition Dates": validate.validate_encounter_dates(conditions_df, 'START', 'STOP'),
    "Condition References Invalid Patient or Organization": validate.encounter_ref_invalid_patient_or_org(conditions_df, patients_df)
}


def create_rejection_report(df, validation_results):
    rejection_list = []
    # has to enter the results in tuple since it comes in as a dictionary, but the reason is not collected here
    for reason, invalid_records in validation_results.items():
        if invalid_records.empty:
            continue
        rejected = invalid_records.copy()
        rejection_list.append(rejected)
    #if the rejection list comes up emty, return an empty dataframe with the same columns as the original df plus the rejection reason column
    if not rejection_list:
        return pd.DataFrame(
            columns=list(df.columns) + ["rejection_reason"]
        )
    #if not empty, concat list into a DF 
    rejection_report = pd.concat(
        rejection_list,
        ignore_index=True
    )
    # using that DF, slap it into another DF that groups by source row, and aggregates all reasons for rejection into a single string
    rejection_report = (
        rejection_report
        .groupby("_source_row", as_index=False, dropna=False)
        .agg({
            **{
                column: "first"
                for column in df.columns
                if column != "_source_row" # change for "_source_row" when doing the encounters rejection report, or just do it for all of them?
            },
            "rejection_reason": lambda reasons:
                "; ".join(sorted(set(reasons)))
        })
    )
    return rejection_report

def create_validation_summary(df, rejection_report):
    total_records = len(df)
    rejected_records = len(rejection_report)
    valid_records = total_records - rejected_records
    failure_percentage = (
        round((rejected_records/total_records) * 100, 2) if total_records > 0 else 0
    )

    summary = pd.DataFrame({
        "metric": [
            "Total Records Checked",
            "Total Rejected Records",
            "Total Valid Records",
            "Failure Percentage"
        ],
        "value": [
            total_records,
            rejected_records,
            valid_records,
            failure_percentage
        ]
    })
    return summary

def create_failure_breakdown(validation_results):
    breakdown = pd.DataFrame({
        "validation_rule" : list(validation_results.keys()),
        "failed_records" : [
            len(records)
            for records in validation_results.values()
        ]
    })
    return breakdown

patient_rejection_report = create_rejection_report(patients_df, patient_validation_results)
patient_rejection_report.to_csv("data/rejected/patient_rejections.csv",index=False)

encounter_rejection_report = create_rejection_report(encounters_df, encounter_validation_results)
encounter_rejection_report.to_csv("data/rejected/encounter_rejections.csv",index=False)

condition_rejection_report = create_rejection_report(conditions_df, condition_validation_results)
condition_rejection_report.to_csv("data/rejected/condition_rejections.csv", index=False)

patients_summary = create_validation_summary(patients_df, patient_validation_results)
patients_summary.to_csv("data/summary/patients_summary.csv", index=False)

encounter_summary = create_validation_summary(patients_df, patient_validation_results)
encounter_summary.to_csv("data/summary/encounter_summary.csv", index=False)

condition_summary = create_validation_summary(patients_df, patient_validation_results)
condition_summary.to_csv("data/summary/condition_summary.csv", index=False)

breakdown = create_failure_breakdown(encounter_validation_results)
breakdown.to_csv("data/summary/breakdown.csv", index=False)

