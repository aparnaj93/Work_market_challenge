import pandas as pd


def read_csv(file):
    df = pd.read_csv(file)
    return df


def normalize_zip(df):
    # Removes rows with bad zips
    df = df.filter(['ZIP code','Complaint ID'])
    mask = (df['ZIP code'].str.contains('X')) | (df['ZIP code'].isnull()) | (df['ZIP code'].str.len() < 5)
    bad_zip = df[mask]
    bad_zip.to_csv('bad_zip.csv', index=False)


def complaints_zip_year(df, year):
    # Rows with proper zips
    clean_zip = df[df['ZIP code'].notnull()]
    mask = (clean_zip['ZIP code'].str.contains('^[0-9]{5}'))
    clean_zip = clean_zip[mask]
    filtered_complaints = clean_zip[clean_zip['Date received'].str[6:] >= year]
    return filtered_complaints


def group_by(df):
    res = df.groupby('ZIP code').size().reset_index(name='Complaints_Count')
    res.to_csv('Group_by_zip.csv', index=False)


file_path = "/Users/jayasuriyanramachandran/Downloads/Consumer_Complaints.csv"
df = read_csv(file_path)
normalize_zip(df)
filter_complaints = complaints_zip_year(df,'2016')
group_by(filter_complaints)
