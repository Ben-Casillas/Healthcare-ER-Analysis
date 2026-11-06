# .isnull().any(axis=1)]
#is null checks every cell for missing data
# any(axis=1) returns the row if at least 1 of its cells is null, change the 1 for another value

import pandas as pd


def test1():
    return "test"

def validate_missing_data(df: pd.DataFrame, req_columns: list):
    return df[df[req_columns].isnull().any(axis=1)]

def validate_duplicate_ids(df: pd.DataFrame, id_column: str):
    return df[df.duplicated(subset=[id_column], keep=False)]

def validate_encounter_dates(df: pd.DataFrame, start_column: str, end_column: str):
    #return rows where the end date is before the start AND the ones that
    return df[(df[end_column].notna()) & (df[start_column] > df[end_column])]

def encounter_ref_invalid_patient_or_org(encounter_df: pd.DataFrame, patient_df: pd.DataFrame, organizations_df: pd.DataFrame):
    return encounter_df[~encounter_df['PATIENT'].isin(patient_df['Id']) | ~encounter_df['ORGANIZATION'].isin(organizations_df['Id'])]

def conditions_ref_invalid_patient_or_encounter(conditions_df: pd.DataFrame, patient_df: pd.DataFrame, encounter_df: pd.DataFrame):
    return conditions_df[~conditions_df['PATIENT'].isin(patient_df['Id']) | ~conditions_df['ENCOUNTER'].isin(encounter_df['Id'])]

