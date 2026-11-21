import pandas as pd
from pathlib import Path

patients = pd.read_csv('Data/raw/patients.csv')
encounters = pd.read_csv('Data/raw/encounters.csv')
organizations = pd.read_csv('Data/raw/organizations.csv')
conditions = pd.read_csv('Data/raw/conditions.csv')

def create_bad_row(df, **updates):
    row = df.iloc[0].copy()
    for column, value in updates.items():
        row[column] = value
    return row

bad_patients = [

    # Missing patient ID
    create_bad_row(patients, Id=""),

    # Duplicate patient ID
    patients.iloc[0].copy(),

    # Missing birthdate
    create_bad_row(patients, BIRTHDATE=""),

    # Impossible birthdate
    create_bad_row(patients, BIRTHDATE="2025-02-30"),

    # Invalid gender category
    create_bad_row(patients, GENDER="UNKNOWN_VALUE"),

    # Latitude outside valid range
    create_bad_row(patients, LAT=150),

    # Longitude outside valid range
    create_bad_row(patients, LON=250)
]

patients_test = pd.concat(
    [patients, pd.DataFrame(bad_patients)],
    ignore_index=True
)

bad_encounters = [

    # Missing encounter ID
    create_bad_row(encounters, Id=""),

    # Duplicate encounter ID
    encounters.iloc[0].copy(),

    # Missing patient ID
    create_bad_row(encounters, PATIENT=""),

    # Patient ID does not exist
    create_bad_row(
        encounters,
        PATIENT="INVALID-PATIENT-001"
    ),

    # Organization ID does not exist
    create_bad_row(
        encounters,
        ORGANIZATION="INVALID-ORG-001"
    ),

    # Invalid start date
    create_bad_row(
        encounters,
        START="not-a-date"
    ),

    # End date before start date
    create_bad_row(
        encounters,
        START="2025-06-15T12:00:00Z",
        STOP="2025-06-14T12:00:00Z"
    ),

    # Missing encounter class
    create_bad_row(
        encounters,
        ENCOUNTERCLASS=""
    ),

    # Negative encounter cost
    create_bad_row(
        encounters,
        BASE_ENCOUNTER_COST=-100
    )
]

encounters_test = pd.concat(
    [encounters, pd.DataFrame(bad_encounters)],
    ignore_index=True
)

bad_organizations = [

    # Missing organization ID
    create_bad_row(organizations, Id=""),

    # Duplicate organization ID
    organizations.iloc[0].copy(),

    # Missing organization name
    create_bad_row(organizations, NAME=""),

    # Invalid latitude
    create_bad_row(organizations, LAT=100),

    # Invalid longitude
    create_bad_row(organizations, LON=-200),

    # Negative revenue
    create_bad_row(organizations, REVENUE=-500),

    # Negative utilization
    create_bad_row(organizations, UTILIZATION=-10)
]

organizations_test = pd.concat(
    [organizations, pd.DataFrame(bad_organizations)],
    ignore_index=True
)

bad_conditions = [

    # Missing patient ID
    create_bad_row(conditions, PATIENT=""),

    # Patient does not exist
    create_bad_row(
        conditions,
        PATIENT="INVALID-PATIENT-002"
    ),

    # Missing encounter ID
    create_bad_row(conditions, ENCOUNTER=""),

    # Encounter does not exist
    create_bad_row(
        conditions,
        ENCOUNTER="INVALID-ENCOUNTER-001"
    ),

    # Missing condition code
    create_bad_row(conditions, CODE=""),

    # Invalid start date
    create_bad_row(conditions, START="not-a-date"),

    # Stop date before start date
    create_bad_row(
        conditions,
        START="2025-06-15",
        STOP="2025-06-14"
    )
]

conditions_test = pd.concat(
    [conditions, pd.DataFrame(bad_conditions)],
    ignore_index=True
)

test_folder = Path("data/invalid")
test_folder.mkdir(parents=True, exist_ok=True)

patients_test.to_csv(
    test_folder / "patients.csv", index=False
)

encounters_test.to_csv(
    test_folder / "encounters.csv", index=False
)

organizations_test.to_csv(
    test_folder / "organizations.csv", index=False
)

conditions_test.to_csv(
    test_folder / "conditions.csv", index=False
)