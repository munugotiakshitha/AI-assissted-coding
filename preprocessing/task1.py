import pandas as pd

# Read the dataset
data = pd.read_csv("shopping_trends.csv")
data.columns = data.columns.str.strip()

print("Original data:")
print(data.head())

# Fill missing values in requested fields if they exist.
# This dataset may use Location instead of City.
for column in ("Age", "age", "Income", "income"):
    if column in data.columns:
        data[column] = pd.to_numeric(data[column], errors="coerce")
        data[column] = data[column].fillna(data[column].median())

city_column = next(
    (column for column in ("City", "city", "Location", "location")
     if column in data.columns),
    None
)

if city_column:
    data[city_column] = data[city_column].fillna("unknown")
    data[city_column] = data[city_column].astype(str).str.strip().str.lower()

# Fill missing categorical values and standardize text.
for column in data.select_dtypes(include="object").columns:
    data[column] = data[column].fillna("unknown").str.strip()

# Remove duplicate records.
data = data.drop_duplicates().copy()

# Encode available categorical columns as numeric codes.
categorical_columns = [
    column for column in ("Gender", "gender", "City", "city", "Location", "location")
    if column in data.columns
]

for column in categorical_columns:
    data[column] = data[column].astype("category").cat.codes

print("\nCleaned data:")
print(data.head())
print("\nMissing values per column:")
print(data.isna().sum())

data.to_csv("customer_data_cleaned.csv", index=False)
print("\nSaved as customer_data_cleaned.csv")