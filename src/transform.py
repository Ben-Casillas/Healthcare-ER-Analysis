import pandas as pd

# write function that standardize all columns

# str.strip() str.lower()/upper() .map() .replace() .fillna() .isin()
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



#method to standardize phone

#method to standardize ssn

#method to standardize race/ethnicity

#method to standardize encounter class

