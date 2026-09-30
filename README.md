# Real-World Data Cleaning Pipeline

A reproducible Python pipeline for cleaning a messy customer dataset and preparing it for analysis.

## Project Overview

This project demonstrates how a real-world dataset can be cleaned programmatically instead of being manually edited.

The pipeline handles:

* Missing and invalid values
* Inconsistent city names
* Invalid age values
* Invalid email values
* Mixed or invalid purchase dates
* Numeric conversion of age and purchase amount
* Duplicate records
* Standardized date formatting

## Dataset

The dataset contains customer purchase information with the following fields:

* `customer_id`
* `name`
* `city`
* `email`
* `age`
* `purchase_amount`
* `purchase_date`

The raw dataset contains 20 rows and 7 columns.

## Cleaning Process

The cleaning pipeline performs the following steps:

1. Loads the raw CSV dataset.
2. Removes completely empty rows.
3. Strips whitespace from column names.
4. Cleans whitespace from text fields.
5. Standardizes city names using title case.
6. Converts age to numeric values.
7. Converts purchase amount to numeric values.
8. Converts purchase dates to datetime.
9. Validates age values and removes invalid values from analysis.
10. Validates email formats.
11. Removes rows missing required fields.
12. Checks for duplicate records.
13. Formats valid purchase dates as `YYYY-MM-DD`.
14. Saves the cleaned dataset.

## Data Quality Results

| Metric                        | Result |
| ----------------------------- | -----: |
| Original rows                 |     20 |
| Cleaned rows                  |     11 |
| Rows removed                  |      9 |
| Original columns              |      7 |
| Cleaned columns               |      7 |
| Completely empty rows removed |      0 |
| Duplicate rows removed        |      0 |
| Invalid age values            |      1 |
| Invalid email values          |      2 |

For a detailed explanation of the data quality results, see [DATA_QUALITY_REPORT.md](DATA_QUALITY_REPORT.md).

## Reproducibility

The complete cleaning process is automated in:

`src/clean_data.py`

To reproduce the cleaning process from the raw dataset, run:

```text
python src/clean_data.py
```

The script reads:

`data/raw_data.csv`

and creates:

`data/processed/cleaned_data.csv`

The output directory is created automatically if it does not already exist.

## Project Structure

```text
real-world-data-cleaning/
│
├── data/
│   ├── raw_data.csv
│   └── processed/
│       └── cleaned_data.csv
│
├── src/
│   └── clean_data.py
│
├── DATA_QUALITY_REPORT.md
├── README.md
└── .gitattributes
```

## Requirements

Python 3.x

Required Python package:

```text
pandas
```

Install pandas with:

```text
pip install pandas
```

## Output

The final cleaned dataset is saved to:

`data/processed/cleaned_data.csv`

The pipeline is designed to be rerunnable from the raw dataset without manually editing the data.
