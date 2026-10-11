"""Data profiling and cleaning functions used by CleanX."""
import pandas as pd

def profile_data(df):
    """Return basic data-quality metrics for a DataFrame."""
    missing_by_column = df.isna().sum()
    return {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "missing_cells": int(missing_by_column.sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "missing_by_column": missing_by_column,
    }

def clean_data(df, remove_duplicates=True, trim_text=True, missing_strategy="Keep missing values"):
    """Clean a copy of a DataFrame and return it with a log of applied changes."""
    cleaned = df.copy()
    changes = []
    if trim_text:
        for column in cleaned.select_dtypes(include=["object", "string"]).columns:
            original = cleaned[column].copy()
            cleaned[column] = cleaned[column].map(lambda value: value.strip() if isinstance(value, str) else value)
            changed = int((original != cleaned[column]).fillna(False).sum())
            if changed:
                changes.append({"Action": "Trim whitespace", "Column": str(column),
                                "Affected records": changed, "Details": "Removed leading/trailing spaces from text values"})
    if remove_duplicates:
        count = int(cleaned.duplicated().sum())
        if count:
            cleaned = cleaned.drop_duplicates().reset_index(drop=True)
            changes.append({"Action": "Remove duplicates", "Column": "All columns",
                            "Affected records": count, "Details": "Removed duplicate rows, keeping the first occurrence"})
    if missing_strategy == "Drop rows with any missing value":
        count = int(cleaned.isna().any(axis=1).sum())
        if count:
            cleaned = cleaned.dropna().reset_index(drop=True)
            changes.append({"Action": "Drop rows with missing values", "Column": "All columns",
                            "Affected records": count, "Details": "Dropped rows containing at least one missing value"})
    elif missing_strategy == "Fill text with 'Unknown' and numbers with median":
        for column in cleaned.columns:
            count = int(cleaned[column].isna().sum())
            if count:
                if pd.api.types.is_numeric_dtype(cleaned[column]):
                    median = cleaned[column].median()
                    fill_value = median if pd.notna(median) else 0
                    details = f"Filled missing numeric values with median ({fill_value})"
                else:
                    fill_value = "Unknown"
                    details = "Filled missing text values with 'Unknown'"
                cleaned[column] = cleaned[column].fillna(fill_value)
                changes.append({"Action": "Fill missing values", "Column": str(column),
                                "Affected records": count, "Details": details})
    elif missing_strategy == "Fill all missing values with 0":
        for column in cleaned.columns:
            count = int(cleaned[column].isna().sum())
            if count:
                cleaned[column] = cleaned[column].fillna(0)
                changes.append({"Action": "Fill missing values", "Column": str(column),
                                "Affected records": count, "Details": "Filled missing values with 0"})
    return cleaned, changes

def build_quality_report(original, cleaned, changes):
    """Create a compact before/after quality report."""
    before, after = profile_data(original), profile_data(cleaned)
    return pd.DataFrame([
        {"Metric": "Rows", "Before": before["rows"], "After": after["rows"]},
        {"Metric": "Columns", "Before": before["columns"], "After": after["columns"]},
        {"Metric": "Missing cells", "Before": before["missing_cells"], "After": after["missing_cells"]},
        {"Metric": "Duplicate rows", "Before": before["duplicate_rows"], "After": after["duplicate_rows"]},
        {"Metric": "Cleaning actions recorded", "Before": 0, "After": len(changes)},
    ])
