
import pandas as pd
from pathlib import Path

# File paths
input_file = Path("data/raw_data.csv")
output_file = Path("data/processed/cleaned_data.csv")

# Read raw data
df = pd.read_csv(input_file)

original_rows = len(df)
original_columns = len(df.columns)

print("Original rows:", original_rows)
print("Original columns:", original_columns)

# Remove completely empty rows
empty_rows = df.isna().all(axis=1).sum()
df = df.dropna(how="all")

# Clean column names
df.columns = df.columns.str.strip()

# Clean text columns
for column in ["name", "city", "email"]:
    df[column] = df[column].astype("string").str.strip()

# Standardize city names
df["city"] = df["city"].str.title()

# Convert age to numeric
df["age"] = pd.to_numeric(df["age"], errors="coerce")

# Convert purchase amount to numeric
df["purchase_amount"] = pd.to_numeric(
    df["purchase_amount"], errors="coerce"
)

# Convert purchase date to datetime
df["purchase_date"] = pd.to_datetime(
    df["purchase_date"], errors="coerce"
)

# Validate age
invalid_age = ((df["age"] < 0) | (df["age"] > 120)).sum()
df.loc[(df["age"] < 0) | (df["age"] > 120), "age"] = pd.NA

# Validate email
email_pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
invalid_email = (~df["email"].str.match(email_pattern, na=False)).sum()
df.loc[
    ~df["email"].str.match(email_pattern, na=False),
    "email"
] = pd.NA

# Count rows with missing required data before dropping
required_columns = [
    "customer_id",
    "name",
    "age",
    "city",
    "email",
    "purchase_amount",
    "purchase_date",
]

invalid_required_rows = df[required_columns].isna().any(axis=1).sum()

# Remove rows with invalid required data
df = df.dropna(subset=required_columns)

rows_after_required_data = len(df)

# Remove duplicate rows
duplicate_rows = df.duplicated().sum()
df = df.drop_duplicates()

# Format date
df["purchase_date"] = df["purchase_date"].dt.strftime("%Y-%m-%d")

# Save cleaned data
output_file.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_file, index=False)

cleaned_rows = len(df)
total_rows_removed = original_rows - cleaned_rows

print("Cleaning completed successfully.")
print("Cleaned rows:", cleaned_rows)
print("Rows removed:", total_rows_removed)
print("Completely empty rows removed:", empty_rows)
print("Rows with invalid/missing required data removed:", invalid_required_rows)
print("Duplicate rows removed:", duplicate_rows)
print("Invalid age values:", invalid_age)
print("Invalid email values:", invalid_email)
print("Saved to:", output_file)
