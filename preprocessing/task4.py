import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("employee_salary.csv")
data.columns = data.columns.str.strip()

# Change these values to match the headings in your CSV.
SALARY_COLUMN = "Salary"
DEPARTMENT_COLUMN = "Department"
LOCATION_COLUMN = "JobLocation"

required_columns = [SALARY_COLUMN, DEPARTMENT_COLUMN, LOCATION_COLUMN]
missing_columns = [column for column in required_columns if column not in data.columns]

if missing_columns:
    raise ValueError(
        f"Missing columns: {missing_columns}. "
        f"Available columns: {list(data.columns)}"
    )

# Clean salary values and remove rows without a usable salary.
data[SALARY_COLUMN] = pd.to_numeric(data[SALARY_COLUMN], errors="coerce")
data = data.dropna(subset=[SALARY_COLUMN]).copy()

# Fill missing text values and standardize department names.
for column in (DEPARTMENT_COLUMN, LOCATION_COLUMN):
    data[column] = data[column].fillna("unknown")
    data[column] = data[column].astype(str).str.strip()

data[DEPARTMENT_COLUMN] = data[DEPARTMENT_COLUMN].str.lower()
data[LOCATION_COLUMN] = data[LOCATION_COLUMN].str.lower()

# Remove salary outliers using the IQR rule.
q1 = data[SALARY_COLUMN].quantile(0.25)
q3 = data[SALARY_COLUMN].quantile(0.75)
iqr = q3 - q1
lower_limit = q1 - 1.5 * iqr
upper_limit = q3 + 1.5 * iqr

data = data[
    data[SALARY_COLUMN].between(lower_limit, upper_limit)
].copy()

# Convert department and job location text into numeric labels.
department_encoder = LabelEncoder()
location_encoder = LabelEncoder()

data["Department_Encoded"] = department_encoder.fit_transform(
    data[DEPARTMENT_COLUMN]
)
data["JobLocation_Encoded"] = location_encoder.fit_transform(
    data[LOCATION_COLUMN]
)

print(data.head())
data.to_csv("employee_salary_cleaned.csv", index=False)
print("Saved as employee_salary_cleaned.csv")