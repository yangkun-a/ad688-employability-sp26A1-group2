import pandas as pd

# Load data
df = pd.read_csv("data/raw/lightcast_job_postings.csv", low_memory=False)

# Basic info
print("Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 3 rows:")
print(df.head(3))

# Key columns we care about
cols = [
    "TITLE_CLEAN",
    "SALARY",
    "SALARY_FROM",
    "SALARY_TO",
    "ORIGINAL_PAY_PERIOD",
    "REMOTE_TYPE_NAME",
    "CITY_NAME",
    "STATE_NAME",
    "SKILLS_NAME"
]

print("\nPreview of key columns:")
print(df[cols].head(10))