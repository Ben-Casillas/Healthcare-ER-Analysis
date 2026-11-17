import pytest
import validate

@pytest.mark.parametrize(
    "column, expected_count",
    [
        ("Id", 1),
        ("NAME", 1),
        ("ADDRESS", 1),
        ("CITY", 0),
        ("STATE", 0),
        ("PHONE", 1)
    ]
)

def test_invalid_organization_missing_values(invalid_organizations_df, column, expected_count):
    result = validate.validate_missing_data(
        invalid_organizations_df, [column]
    )
    assert len(result) == expected_count

def test_organization_duplicate_ids(invalid_organizations_df):
    result = validate.validate_duplicate_ids(invalid_organizations_df, 'Id')
    assert(len(result) == 7)