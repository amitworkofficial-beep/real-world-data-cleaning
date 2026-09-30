# Data Quality Report

## Project

Real-World Data Cleaning Pipeline

## 1. Dataset Overview

The raw dataset contains customer information including customer ID, name, city, email, age, purchase amount, and purchase date.

The raw dataset contained **20 rows and 7 columns** before cleaning.

After applying the reproducible cleaning pipeline, the dataset contains **11 rows and 7 columns**.

## 2. Before and After Summary

| Metric                 | Before Cleaning | After Cleaning |
| ---------------------- | --------------: | -------------: |
| Rows                   |              20 |             11 |
| Columns                |               7 |              7 |
| Rows removed           |               0 |              9 |
| Completely empty rows  |               0 |              0 |
| Duplicate rows removed |               0 |              0 |

A total of **9 rows were removed** during the cleaning process.

## 3. Cleaning Decisions

### Column names

Whitespace was removed from column names to ensure consistent column references.

### Text fields

Whitespace was removed from the `name`, `city`, and `email` fields.

### City names

City names were standardized using title case so that inconsistent capitalization is normalized.

### Age

The `age` column was converted to numeric values.

Age values below 0 or above 120 were treated as invalid and converted to missing values.

The dataset contained **1 invalid age value**.

### Purchase amount

The `purchase_amount` column was converted to numeric values. Values that could not be converted were treated as missing.

### Purchase date

The `purchase_date` column was converted to datetime values. Invalid dates were treated as missing.

Valid dates were finally stored in `YYYY-MM-DD` format.

### Email

Email values were checked against a basic email format pattern.

Invalid email values were treated as missing.

The dataset contained **2 invalid email values**.

### Required data

Rows missing any required field were removed because the pipeline requires complete records for analysis.

A total of **9 rows were removed because of invalid or missing required data**.

### Duplicate records

Duplicate rows were checked and removed.

**0 duplicate rows were found.**

## 4. Rows Removed

The pipeline removed **9 rows in total**.

Breakdown reported by the cleaning script:

* Completely empty rows: **0**
* Rows with invalid or missing required data: **9**
* Duplicate rows: **0**

The invalid age and email values contributed to the invalid/missing required-data check when those values were converted to missing values.

## 5. Reproducibility

The cleaning process is implemented in `src/clean_data.py`.

The pipeline can be rerun from the raw dataset using:

```text
python src/clean_data.py
```

The script reads the raw data from:

`data/raw_data.csv`

and writes the cleaned dataset to:

`data/processed/cleaned_data.csv`

No manual data editing is required.

## 6. Final Result

The cleaning pipeline reduced the dataset from **20 rows to 11 rows** while standardizing text, validating important fields, converting data types, checking required fields, checking duplicates, and formatting dates consistently.

The resulting dataset is stored as:

`data/processed/cleaned_data.csv`
