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
    test = df.index[df[date_column].notna()].tolist()
    for index in test:
        date_value2 = df.at[index, date_column]
        date_value = pd.to_datetime(date_value2, errors="coerce")
        # date_value = pd.to_datetime(index)
        standardized_date = date_value.strftime("%m/%d/%Y",)
        df.at[index, date_column] = standardized_date
    return df


#method to standardize the genders

#method to standardize phone

#method to standardize ssn

#method to standardize race/ethnicity

#method to standardize encounter class

