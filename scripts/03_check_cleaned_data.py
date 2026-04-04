import pandas as pd

df = pd.read_csv("data/processed/lightcast_cleaned.csv", low_memory=False)

print("Shape:", df.shape)

print("\nMissing values in salary_clean:")
print(df["salary_clean"].isna().sum())

print("\nORIGINAL_PAY_PERIOD value counts:")
print(df["ORIGINAL_PAY_PERIOD"].value_counts(dropna=False).head(20))

print("\nREMOTE_TYPE_NAME value counts:")
print(df["REMOTE_TYPE_NAME"].value_counts(dropna=False).head(20))

print("\nSample TITLE_CLEAN:")
print(df["TITLE_CLEAN"].dropna().head(10))

print("\nSample SKILLS_NAME:")
print(df["SKILLS_NAME"].dropna().head(5))