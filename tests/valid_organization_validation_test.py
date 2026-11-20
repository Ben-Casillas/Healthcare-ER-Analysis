import pytest
import validate

@pytest.mark.parametrize(
    "column, expected_count",
    [
        ("Id", 0),
        ("NAME", 0),
        ("ADDRESS", 0),
        ("CITY", 0),
        ("STATE", 0),
        ("PHONE", 0)
    ]
)

def test_valid_organization_missing_values(valid_organizations_df, column, expected_count):
    result = validate.validate_missing_data(
        valid_organizations_df, [column]
    )
    assert len(result) == expected_count

def test_organization_duplicate_ids(valid_organizations_df):
    result = validate.validate_duplicate_ids(valid_organizations_df, 'Id')
    assert(len(result) == 0)