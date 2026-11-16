import pytest
import validate
import pandas as pd

organizations_df = pd.read_csv('./Data/invalid/organizations.csv')

def test_len_missing_id_organization():
    assert(len(validate.validate_missing_data(organizations_df, ['Id'])) == 2)

def test_len_missing_name_organization():
    assert(len(validate.validate_missing_data(organizations_df, ['NAME'])) == 1)

def test_len_missing_address_organization():
    assert(len(validate.validate_missing_data(organizations_df, ['ADDRESS'])) == 1)

def test_len_missing_city_organization():
    with pytest.raises(AssertionError):
        assert(len(validate.validate_missing_data(organizations_df, ['CITY'])) != 0)

def test_len_missing_state_organization():
    with pytest.raises(AssertionError):
        assert(len(validate.validate_missing_data(organizations_df, ['STATE'])) != 0)

def test_len_missing_phone_organization():
    assert(len(validate.validate_missing_data(organizations_df, ['PHONE'])) == 1)

def test_organization_duplicate_ids():
    assert(len(validate.validate_duplicate_ids(organizations_df, 'Id')) == 9)

# ask people what other tests i should run