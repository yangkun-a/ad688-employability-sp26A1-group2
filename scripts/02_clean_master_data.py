import pandas as pd
import numpy as np

# Load raw data
df = pd.read_csv("data/raw/lightcast_job_postings.csv", low_memory=False)

# Keep useful columns
keep_cols = [
    "ID",
    "POSTED",
    "EXPIRED",
    "DURATION",
    "TITLE_RAW",
    "TITLE_CLEAN",
    "COMPANY_NAME",
    "SALARY",
    "SALARY_FROM",
    "SALARY_TO",
    "ORIGINAL_PAY_PERIOD",
    "REMOTE_TYPE_NAME",
    "LOCATION",
    "CITY_NAME",
    "STATE_NAME",
    "NAICS2_NAME",
    "NAICS3_NAME",
    "LIGHTCAST_SECTORS_NAME",
    "SKILLS_NAME",
    "SPECIALIZED_SKILLS_NAME",
    "COMMON_SKILLS_NAME",
    "SOFTWARE_SKILLS_NAME",
    "MIN_YEARS_EXPERIENCE",
    "MAX_YEARS_EXPERIENCE",
    "EDUCATION_LEVELS_NAME"
]

df = df[keep_cols].copy()

# Drop duplicate job IDs
df = df.drop_duplicates(subset="ID")

# Standardize missing values
df = df.replace(r"^\s*$", np.nan, regex=True)

# Create one cleaned salary column
def get_salary(row):
    if pd.notna(row["SALARY"]):
        return row["SALARY"]
    elif pd.notna(row["SALARY_FROM"]) and pd.notna(row["SALARY_TO"]):
        return (row["SALARY_FROM"] + row["SALARY_TO"]) / 2
    elif pd.notna(row["SALARY_FROM"]):
        return row["SALARY_FROM"]
    elif pd.notna(row["SALARY_TO"]):
        return row["SALARY_TO"]
    else:
        return np.nan

df["salary_clean"] = df.apply(get_salary, axis=1)


def convert_to_annual(row):
    salary = row["salary_clean"]
    period = str(row["ORIGINAL_PAY_PERIOD"]).lower()

    if pd.isna(salary):
        return np.nan

    if period == "year":
        return salary
    elif period == "month":
        return salary * 12
    elif period == "week":
        return salary * 52
    elif period == "day":
        return salary * 260
    elif period == "hour":
        return salary * 2080
    else:
        return np.nan

df["salary_annual"] = df.apply(convert_to_annual, axis=1)

df["REMOTE_TYPE_NAME"] = df["REMOTE_TYPE_NAME"].replace("[None]", np.nan)

df = df[df["salary_annual"].notna()]

# Save cleaned file
df.to_csv("data/processed/lightcast_cleaned.csv", index=False)

print("Done.")
print("Shape:", df.shape)
print(df.head())