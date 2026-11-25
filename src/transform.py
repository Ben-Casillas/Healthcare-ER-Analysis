import pandas as pd
import re

# write function that standardize all columns

#value_counts() .unique() .isin()
# str.fullmatch() str.zfill()
# str.extract() #str.startswith()
#str.normalize()
#pd.to_numeric() .round() .astype() .between() .clip()

#method to standardize the dates
def standardize_date(df: pd.DataFrame, date_column: str):
    if date_column not in df.columns:
        return
    # for each row in the date_column
    for index in df.index[df[date_column].notna()].tolist():
        ts_date = df.at[index, date_column]
        date_value = pd.to_datetime(ts_date, errors="coerce")
        standardized_date = date_value.strftime("%m/%d/%Y",)
        df.at[index, date_column] = standardized_date
    return df

#standarize gender, still must account for X123 and Unknown_Category
def standardize_gender(df: pd.DataFrame, column: str):
    gender_mapping = {
        "male": "M",
        "man": "M",
        "m": "M",
        "female": "F",
        "woman": "F",
        "w": "W",
        "f": "F"
    }
    if column not in df.columns:
        return

    cleaned = df[column].str.strip().str.casefold()
    df[column] = cleaned.map(gender_mapping).fillna("Unknown")
    return df

#method to standardize ssn
def standardize_ssn(df: pd.DataFrame, column: str):
    if column not in df.columns:
        return
    for index in df.index[df[column].notna()].tolist():
        value = df.at[index, column]
        digits = re.sub(r"\D", "", str(value))
        formatted_digits = f"{digits[:3]}-{digits[3:5]}-{digits[5:]}"
        df.at[index, column] = formatted_digits
    return df

#method to standardize race
def standardize_race(df: pd.DataFrame, column: str):
    if column not in df.columns:
        return
    race_mapping = {
        "white": "white",
        "caucasian": "white",
        "black": "black",
        "african american": "black",
        "asian": "asian",
        "native": "native",
        "hawaiian": "hawaiian"
    }
    cleaned = df[column].str.strip().str.casefold()
    df[column] = cleaned.map(race_mapping).fillna("Unknown")
    return df    

#method to standardize phone (Org)
def standardize_phone(df: pd.DataFrame, column: str):
    if column not in df.columns:
        return
    for index in df.index[df[column].notna()].tolist():
        value = df.at[index, column]
        digits = re.sub(r"\D", "", str(value))

#method to standardize text

#method to standardize encounter class

