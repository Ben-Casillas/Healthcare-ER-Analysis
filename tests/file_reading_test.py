import pytest
import pandas as pd
import validate 

def read_empty(df):
    return  pd.DataFrame(columns=list(df.columns))

def test_correct_row_count_patients(invalid_patients_df):
    assert(len(invalid_patients_df) == 119)
    
def test_correct_row_count_encounters(invalid_encounters_df):
    assert(len(invalid_encounters_df) == 5070)
    
def test_correct_row_count_orgs(invalid_organizations_df):
    assert(len(invalid_organizations_df) == 274)
    
def test_correct_row_count_conditions(invalid_conditions_df):
    assert(len(invalid_conditions_df) == 3394)
