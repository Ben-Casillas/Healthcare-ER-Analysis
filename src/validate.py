import pandas as pd

patients_df = pd.read_csv('Data/invalid/patients.csv')
encounters_df = pd.read_csv('Data/invalid/encounters.csv')

pd.options.display.max_rows = None

# .isnull().any(axis=1)]
#is null checks every cell for missing data
# any(axis=1) returns the row if at least 1 of its cells is null, change the 1 for another value
def validate_missing_data(df, req_columns):
    return print(df[df[req_columns].isnull().any(axis=1)])

def validate_duplicate_ids(df, id_column):
    return print(df[df.duplicated(subset=[id_column], keep=False)])

def validate_encounter_dates(df, start_column, end_column):
    if not df[end_column].isnull().any():
        return print(df[df[start_column] > df[end_column]])
    else:
        return print(df[df[start_column].isnull().any(axis=1)])



# validate_missing_data(patients_df, ['Id', 'BIRTHDATE', 'SSN', 'FIRST', 'LAST'])
# validate_missing_data(encounters_df, ['Id', 'START', 'PATIENT', 'ORGANIZATION', 'PROVIDER', 'ENCOUNTERCLASS', 'CODE'])

# validate_duplicate_ids(patients_df, 'Id')
# validate_duplicate_ids(encounters_df, 'Id')