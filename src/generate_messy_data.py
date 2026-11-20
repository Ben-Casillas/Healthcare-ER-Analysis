
import pandas as pd
import random
import re
from pathlib import Path

# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

random.seed(42)

RAW_DIR = Path("../Data/raw")
MESSY_DIR = Path("../Data/messy")

MESSY_DIR.mkdir(parents=True, exist_ok=True)

# Percentage of eligible records to modify per column
MODIFICATION_RATE = 0.20

# --------------------------------------------------
# GENERAL HELPER FUNCTIONS
# --------------------------------------------------

def modify_column(df, column, function, rate=MODIFICATION_RATE):
    """Randomly modifies a percentage of nonmissing values."""

    if column not in df.columns:
        return

    eligible = df.index[df[column].notna()].tolist()

    count = int(len(eligible) * rate)

    selected = random.sample(eligible, min(count, len(eligible)))

    for index in selected:
        df.at[index, column] = function(df.at[index, column])


def format_date(value):
    """Returns the same date in a randomly selected format."""

    date = pd.to_datetime(value, errors="coerce")

    if pd.isna(date):
        return value

    formats = [
        "%m/%d/%Y",
        "%d-%b-%Y",
        "%Y/%m/%d",
        "%Y%m%d",
        "%m-%d-%Y",
        "%d/%m/%Y",
        "%Y-%m-%d"
    ]

    return date.strftime(random.choice(formats))


def format_timestamp(value):
    """Returns the same timestamp in a different format."""

    date = pd.to_datetime(value, errors="coerce")

    if pd.isna(date):
        return value

    formats = [
        "%m/%d/%Y %H:%M",
        "%Y/%m/%d %H:%M:%S",
        "%d-%b-%Y %I:%M %p",
        "%Y-%m-%dT%H:%M:%S",
        "%m-%d-%Y %H:%M:%S"
    ]

    return date.strftime(random.choice(formats))


def format_ssn(value):
    """Changes SSN punctuation without changing the digits."""

    digits = re.sub(r"\D", "", str(value))

    if len(digits) != 9:
        return value

    formats = [
        lambda x: x,
        lambda x: f"{x[:3]}-{x[3:5]}-{x[5:]}",
        lambda x: f"{x[:3]} {x[3:5]} {x[5:]}",
        lambda x: f"{x[:3]}.{x[3:5]}.{x[5:]}"
    ]

    return random.choice(formats)(digits)


def format_phone(value):
    """Changes phone number formatting."""

    digits = re.sub(r"\D", "", str(value))

    if len(digits) == 11 and digits.startswith("1"):
        digits = digits[1:]

    if len(digits) != 10:
        return value

    formats = [
        lambda x: x,
        lambda x: f"{x[:3]}-{x[3:6]}-{x[6:]}",
        lambda x: f"({x[:3]}) {x[3:6]}-{x[6:]}",
        lambda x: f"{x[:3]}.{x[3:6]}.{x[6:]}",
        lambda x: f"+1 {x[:3]} {x[3:6]} {x[6:]}"
    ]

    return random.choice(formats)(digits)


def messy_text(value):
    """Introduces capitalization and whitespace inconsistencies."""

    variations = [
        lambda x: str(x).upper(),
        lambda x: str(x).lower(),
        lambda x: str(x).title(),
        lambda x: f"  {x}  ",
        lambda x: str(x).replace(" ", "  ")
    ]

    return random.choice(variations)(value)


# --------------------------------------------------
# PATIENT DATA TRANSFORMATIONS
# --------------------------------------------------

def mess_up_patients(df):
    # Date variations
    for column in ["BIRTHDATE", "DEATHDATE"]:
        modify_column(df, column, format_date)

    # SSN variations
    modify_column(df, "SSN", format_ssn)

    # Phone variations
    modify_column(df, "PHONE", format_phone)

    # Gender variations
    gender_variations = {
        "M": ["Male", "male", "m", " MALE ", "Man"],
        "F": ["Female", "female", "f", " FEMALE ", "Woman"]
    }

    def change_gender(value):
        choices = gender_variations.get(str(value).strip().upper())

        if choices:
            return random.choice(choices)

        return value

    modify_column(df, "GENDER", change_gender)

    # Race variations
    race_variations = {
        "white": ["White", "WHITE", " white ", "Caucasian"],
        "black": ["Black", "BLACK", " black ", "African American"],
        "asian": ["Asian", "ASIAN", " asian "],
        "native": ["Native", "NATIVE", " native "],
        "hawaiian": ["Hawaiin", "HAWAIIN", "hawaiian "]
    }

    def change_race(value):
        choices = race_variations.get(str(value).strip().lower())

        if choices:
            return random.choice(choices)

        return value

    modify_column(df, "RACE", change_race)

    # Ethnicity capitalization and whitespace
    modify_column(df, "ETHNICITY", messy_text)

    # Names
    for column in ["FIRST", "MIDDLE", "LAST", "MAIDEN"]:
        modify_column(df, column, messy_text)

    # ZIP codes
    def messy_zip(value):
        value = str(value).strip()

        if value.isdigit():
            return f" {value} "

        return value

    modify_column(df, "ZIP", messy_zip)

    # Missing optional values
    for column in ["PHONE", "SSN", "MIDDLE", "MAIDEN", "SUFFIX"]:
        if column in df.columns:
            modify_column(
                df,
                column,
                lambda x: pd.NA,
                rate=0.05
            )

    return df


# --------------------------------------------------
# ENCOUNTER DATA TRANSFORMATIONS
# --------------------------------------------------

def mess_up_encounters(df):

    # Date and timestamp variations
    modify_column(df, "START", format_timestamp)
    modify_column(df, "STOP", format_timestamp)

    # Encounter class variations
    encounter_variations = {
        "ambulatory": ["Ambulatory", "AMBULATORY", " ambulatory "],
        "emergency": ["ER", "Emergency", "Emergency Room"],
        "inpatient": ["IP", "Inpatient", "INPATIENT"],
        "outpatient": ["OP", "Outpatient", "OUTPATIENT"],
        "urgentcare": ["Urgent Care", "URGENT CARE", "urgent care"],
        "wellness": ["Wellness", "WELLNESS", " wellness "],
        "sickness": ["Sick Visit", "SICKNESS", "sickness"]
    }

    def change_encounter_class(value):
        choices = encounter_variations.get(str(value).strip().lower())

        if choices:
            return random.choice(choices)

        return value

    modify_column(
        df,
        "ENCOUNTERCLASS",
        change_encounter_class
    )

    # Description inconsistencies
    modify_column(df, "DESCRIPTION", messy_text)

    # Missing optional values
    for column in ["STOP", "REASONCODE", "REASONDESCRIPTION"]:
        modify_column(
            df,
            column,
            lambda x: pd.NA,
            rate=0.05
        )

    return df


# --------------------------------------------------
# ORGANIZATION DATA TRANSFORMATIONS
# --------------------------------------------------

def mess_up_organizations(df):

    modify_column(df, "NAME", messy_text)
    modify_column(df, "ADDRESS", messy_text)
    modify_column(df, "CITY", messy_text)
    modify_column(df, "STATE", messy_text)
    modify_column(df, "PHONE", format_phone)

    # ZIP inconsistencies
    modify_column(
        df,
        "ZIP",
        lambda x: f" {str(x).strip()} "
    )

    return df


# --------------------------------------------------
# CONDITION DATA TRANSFORMATIONS
# --------------------------------------------------

def mess_up_conditions(df):

    for column in ["START", "STOP"]:
        modify_column(df, column, format_date)

    modify_column(df, "DESCRIPTION", messy_text)

    modify_column(
        df,
        "STOP",
        lambda x: pd.NA,
        rate=0.05
    )

    return df


# --------------------------------------------------
# INTRODUCE INTENTIONALLY INVALID DATA
# --------------------------------------------------

def introduce_invalid_values(df, column, values):

    if column not in df.columns:
        return

    eligible = df.index[df[column].notna()].tolist()

    if not eligible:
        return

    count = min(max(1, int(len(eligible) * 0.02)), len(eligible))

    selected = random.sample(eligible, count)

    for index in selected:
        df.at[index, column] = random.choice(values)


def introduce_invalid_records(patients, encounters, organizations, conditions):

    # Invalid dates
    introduce_invalid_values(
        patients, "BIRTHDATE",
        ["not-a-date", "2024-99-99", "32/13/2024"]
    )

    introduce_invalid_values(
        encounters, "START",
        ["invalid-date", "2024-99-99", "not available"]
    )

    # Invalid SSNs
    introduce_invalid_values(
        patients, "SSN",
        ["12345", "ABC-12-3456", "1234567890"]
    )

    # Invalid phone numbers
    introduce_invalid_values(
        patients, "PHONE",
        ["123", "abcdefghij", "123-45-678"]
    )

    # Unknown categorical values
    introduce_invalid_values(
        patients, "GENDER",
        ["UNKNOWN_CATEGORY", "X123"]
    )

    introduce_invalid_values(
        encounters, "ENCOUNTERCLASS",
        ["UNKNOWN_CLASS", "INVALID_TYPE"]
    )

    # Invalid numeric values
    introduce_invalid_values(
        encounters, "TOTAL_CLAIM_COST",
        ["not-a-number", "$INVALID"]
    )

    # Broken patient references
    if "PATIENT" in encounters.columns:
        eligible = encounters.index[
            encounters["PATIENT"].notna()
        ].tolist()

        if eligible:
            index = random.choice(eligible)
            encounters.at[index, "PATIENT"] = "INVALID_PATIENT_ID"

    # Broken organization references
    if "ORGANIZATION" in encounters.columns:
        eligible = encounters.index[
            encounters["ORGANIZATION"].notna()
        ].tolist()

        if eligible:
            index = random.choice(eligible)
            encounters.at[index, "ORGANIZATION"] = "INVALID_ORG_ID"

    # Broken encounter references
    if "ENCOUNTER" in conditions.columns:
        eligible = conditions.index[
            conditions["ENCOUNTER"].notna()
        ].tolist()

        if eligible:
            index = random.choice(eligible)
            conditions.at[index, "ENCOUNTER"] = "INVALID_ENCOUNTER_ID"

    return patients, encounters, organizations, conditions


# --------------------------------------------------
# INTRODUCE DUPLICATE RECORDS
# --------------------------------------------------

def introduce_duplicates(df, rate=0.01):

    if df.empty:
        return df

    count = max(1, int(len(df) * rate))

    duplicates = df.sample(
        n=min(count, len(df)),
        random_state=42
    )

    return pd.concat(
        [df, duplicates],
        ignore_index=True
    )


# --------------------------------------------------
# MAIN EXECUTION
# --------------------------------------------------

def main():

    files = {
        "patients": "patients.csv",
        "encounters": "encounters.csv",
        "organizations": "organizations.csv",
        "conditions": "conditions.csv"
    }

    datasets = {}

    # Read source files
    for name, filename in files.items():

        path = RAW_DIR / filename

        if not path.exists():
            raise FileNotFoundError(
                f"Missing source file: {path}"
            )

        datasets[name] = pd.read_csv(path, dtype=str)

    patients = datasets["patients"]
    encounters = datasets["encounters"]
    organizations = datasets["organizations"]
    conditions = datasets["conditions"]

    # Record original counts
    original_counts = {
        name: len(df)
        for name, df in datasets.items()
    }

    # Apply transformations
    patients = mess_up_patients(patients)
    encounters = mess_up_encounters(encounters)
    organizations = mess_up_organizations(organizations)
    conditions = mess_up_conditions(conditions)

    # Introduce invalid records
    patients, encounters, organizations, conditions = (
        introduce_invalid_records(
            patients,
            encounters,
            organizations,
            conditions
        )
    )

    # Introduce duplicates
    patients = introduce_duplicates(patients)
    encounters = introduce_duplicates(encounters)
    conditions = introduce_duplicates(conditions)

    final_datasets = {
        "patients": patients,
        "encounters": encounters,
        "organizations": organizations,
        "conditions": conditions
    }

    # Export messy files
    print("\nMESSY DATA GENERATION SUMMARY")
    print("-" * 45)

    for name, df in final_datasets.items():

        output_path = MESSY_DIR / f"{name}.csv"

        df.to_csv(output_path, index=False)

        print(
            f"{name}: "
            f"{original_counts[name]:,} original records -> "
            f"{len(df):,} messy records"
        )

        print(f"Saved to: {output_path}")

    print("\nMessy dataset generation complete!")


if __name__ == "__main__":
    main()
