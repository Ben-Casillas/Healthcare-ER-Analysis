import pandas as pd
import validate

patients_df = pd.read_csv('Data/invalid/patients.csv')
encounters_df = pd.read_csv('Data/invalid/encounters.csv')
organizations_df = pd.read_csv('Data/invalid/organizations.csv')
conditions_df = pd.read_csv('Data/invalid/conditions.csv')

encounter_validation_results = {
    "Missing Required Data": validate.validate_missing_data(encounters_df, ['Id', 'START', 'PATIENT', 'ORGANIZATION', 'PROVIDER']),
    "Duplicate IDs": validate.validate_duplicate_ids(encounters_df, 'Id'),
    "Invalid Encounter Dates": validate.validate_encounter_dates(encounters_df, 'START', 'STOP'),
    "Encounter References Invalid Patient or Organization": validate.encounter_ref_invalid_patient_or_org(encounters_df, patients_df, organizations_df)
}
patient_validation_results = {
    "Missing Required Data": validate.validate_missing_data(patients_df, ['Id', 'BIRTHDATE', 'SSN', 'FIRST', 'LAST']),
    "Duplicate IDs": validate.validate_duplicate_ids(patients_df, 'Id')
}
condition_validation_results = {
    "Missing Required Data": validate.validate_missing_data(conditions_df, ['START', 'PATIENT', 'ENCOUNTER', 'CODE']),
    "Invalid Condition Dates": validate.validate_encounter_dates(conditions_df, 'START', 'STOP'),
    "Condition References Invalid Patient or Organization": validate.encounter_ref_invalid_patient_or_org(conditions_df, patients_df)
}

def create_rejection_report(df, validation_results):
    rejection_list = []
    for reason, invalid_records in validation_results.items():
        if invalid_records.empty:
            continue
        rejected = invalid_records.copy()
        # rejected["rejection_reason"] = reason
        rejection_list.append(rejected)
    if not rejection_list:
        return pd.DataFrame(
            columns=list(df.columns) + ["rejection_reason"]
        )
    rejection_report = pd.concat(
        rejection_list,
        ignore_index=True
    )
    return rejection_report


encounter_rejection_report = create_rejection_report(encounters_df, encounter_validation_results)
encounter_rejection_report.to_csv(
    "data/rejected/encounter_rejections.csv",
    index=False
)

patient_rejection_report = create_rejection_report(patients_df, patient_validation_results)
patient_rejection_report.to_csv(
    "data/rejected/patient_rejections.csv",
    index=False
)

condition_rejection_report = create_rejection_report(conditions_df, condition_validation_results)
condition_rejection_report.to_csv(
    "data/rejected/condition_rejections.csv",
    index=False
)