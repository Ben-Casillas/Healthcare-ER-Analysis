import pytest
import pandas as pd

patients_df = pd.read_csv('./Data/invalid/patients.csv')
encounters_df = pd.read_csv('./Data/invalid/encounters.csv')
organizations_df = pd.read_csv('./Data/invalid/organizations.csv')
conditions_df = pd.read_csv('./Data/invalid/conditions.csv')

def test_correct_row_count_patients():
    assert(len(patients_df) == 119)
    
def test_correct_row_count_encounters():
    assert(len(encounters_df) == 5070)
    
def test_correct_row_count_orgs():
    assert(len(organizations_df) == 274)
    
def test_correct_row_count_conditions():
    assert(len(conditions_df) == 3394)
