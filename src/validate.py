# .isnull().any(axis=1)]
#is null checks every cell for missing data
# any(axis=1) returns the row if at least 1 of its cells is null, change the 1 for another value

import pandas as pd

def validate_missing_data(df: pd.DataFrame, req_columns: list):
    invalid_records = df[df[req_columns].isnull().any(axis=1)]
    invalid_records["rejection_reason"] = invalid_records.apply(
        lambda row: ", ".join(
            [f"Missing {col} Column" for col in req_columns if pd.isnull(row[col])]
        ),
        axis=1
    )

    return invalid_records

def validate_duplicate_ids(df: pd.DataFrame, id_column: str):
    invalid_records = df[df.duplicated(subset=[id_column], keep=False)]
    invalid_records["rejection_reason"] = "Duplicate ID"
    return invalid_records

def validate_encounter_dates(df: pd.DataFrame, start_column: str, end_column: str):
    invalid_records = df[(df[end_column].notna()) & (df[start_column] > df[end_column])]
    invalid_records["rejection_reason"] = "Stop date is before start date"
    return invalid_records

def encounter_ref_invalid_patient_or_org(encounter_df: pd.DataFrame, patient_df: pd.DataFrame, organizations_df: pd.DataFrame = None):
    if organizations_df is None:
        invalid_records = encounter_df[~encounter_df['PATIENT'].isin(patient_df['Id'])]
        invalid_records["rejection_reason"] = "Invalid Patient ID"
        return invalid_records
    else:
        invalid_records = encounter_df[~encounter_df['PATIENT'].isin(patient_df['Id']) | ~encounter_df['ORGANIZATION'].isin(organizations_df['Id'])]
        invalid_records["rejection_reason"] = "Invalid Patient or Organization ID"
        return invalid_records

def conditions_ref_invalid_patient_or_encounter(conditions_df: pd.DataFrame, patient_df: pd.DataFrame, encounter_df: pd.DataFrame):
    invalid_records = conditions_df[~conditions_df['PATIENT'].isin(patient_df['Id']) | ~conditions_df['ENCOUNTER'].isin(encounter_df['Id'])]
    invalid_records["rejection_reason"] = "Invalid Patient or Encounter ID"
    return invalid_records
