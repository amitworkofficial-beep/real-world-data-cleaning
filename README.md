# Real-World Data Cleaning Pipeline

A reproducible data cleaning pipeline for transforming a messy dataset into an analysis-ready dataset.

## Project Overview

This project demonstrates how Python and pandas can be used to clean and standardize messy real-world data.

The raw dataset contains customer information, including customer IDs, names, ages, cities, email addresses, purchase amounts, and purchase dates.

## Dataset

The raw dataset contains 20 records and 7 columns.

The following data quality issues were intentionally included:

- Missing values
- Invalid age values
- Negative age values
- Invalid email addresses
- Inconsistent city capitalization
- Missing purchase amounts
- Invalid purchase dates
- Duplicate records

## Cleaning Process

The cleaning pipeline performs the following steps:

1. Loads the raw CSV dataset using pandas.
2. Removes completely empty rows.
3. Cleans column names and text fields.
4. Standardizes city names.
5. Converts age values to numeric values.
6. Converts purchase amounts to numeric values.
7. Converts purchase dates to a consistent date format.
8. Identifies invalid ages and treats them as missing.
9. Validates email addresses.
10. Removes rows with invalid or missing required values.
11. Removes duplicate rows.
12. Saves the cleaned dataset as a new CSV file.

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
├── outputs/
│
└── README.md