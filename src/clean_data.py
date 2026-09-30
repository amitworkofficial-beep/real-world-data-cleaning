import pandas as pd
from pathlib import Path

# File paths
input_file = Path("data/raw_data.csv")
output_file = Path("data/processed/cleaned_data.csv")

# Read raw data
df = pd.read_csv(input_file)

print("Original rows:", len(df))
print("Original columns:", len(df.columns))

# Remove completely empty rows
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
df.loc[(df["age"] < 0) | (df["age"] > 120), "age"] = pd.NA

# Validate email
email_pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
df.loc[~df["email"].str.match(email_pattern, na=False), "email"] = pd.NA

# Remove rows with invalid required data
df = df.dropna(
    subset=[
        "customer_id",
        "name",
        "age",
        "city",
        "email",
        "purchase_amount",
        "purchase_date",
    ]
)

# Remove duplicate rows
df = df.drop_duplicates()

# Format date
df["purchase_date"] = df["purchase_date"].dt.strftime("%Y-%m-%d")

# Save cleaned data
output_file.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_file, index=False)

print("Cleaning completed successfully.")
print("Cleaned rows:", len(df))
print("Saved to:", output_file)